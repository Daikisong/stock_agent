# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
output_file: e2r_stock_web_v12_residual_round_R5_loop_139_L5_CONSUMER_BRAND_RETAIL_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md
selected_round: R5
selected_loop: 139
selection_basis: docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket: Priority 0
round_schedule_status: coverage_index_selected
round_sector_consistency: pass
large_sector_id: L5_CONSUMER_BRAND_RETAIL
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: GLOBAL_BRAND_CHANNEL_INVENTORY_SELL_THROUGH_MARGIN_FAIL
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - inventory_sell_through_margin_stress_test
  - canonical_archetype_compression
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
```

This is the corrected valid run after C02 reached the local 30-row stability threshold at loop138. C19 is the next Priority 0 coverage gap in the No-Repeat Index.

This loop adds 3 new independent C19 rows and moves C19 from static 24 rows to projected 27 rows. It still needs 3 rows to reach the 30-row stability threshold.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_2_rolling_calibrated_proxy`; rollback reference is `e2r_2_1_stock_web_calibrated`.

Already-applied global axes are not re-proposed. This loop stress-tests them inside C19:

- `stage2_actionable_evidence_bonus`
- `price_only_blowoff_blocks_positive_stage`
- `full_4b_requires_non_price_evidence`
- `hard_4c_thesis_break_routes_to_4c`

## 2. Round / Large Sector / Canonical Archetype Scope

```text
R5 -> L5_CONSUMER_BRAND_RETAIL
C19 -> C19_BRAND_RETAIL_INVENTORY_MARGIN
```

C19 is the brand / retail / inventory-margin archetype. Revenue growth is the shop window; sell-through, inventory turns, receivable quality, OPM and cash conversion are the stockroom. If the stockroom is clogged, the window display is not enough.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index snapshot used for this run:

| item | value |
|---|---:|
| C19 static rows | 24 |
| C19 need to 30 | 6 |
| C19 need to 50 | 26 |
| C19 investigation point | 재고/매출채권/OPM/sell-through로 성장 재고와 channel stuffing 분리 |
| local previous C19 rows in this session | 0 |
| this loop projected rows | 27 |

Selected C19 symbols:

| symbol | company | status |
|---|---|---|
| 383220 | F&F | new local C19 channel inventory false-positive |
| 081660 | 휠라홀딩스 | new local C19 inventory normalization buffer |
| 298540 | 더네이쳐홀딩스 | new local C19 growth inventory sell-through failure |

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
| 383220 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, weight 0.95 |
| 081660 / 2024-03-06 | true | true | clean_entry_window_old_profile_caveat_but_2024_share_count_drift_watch | true, weight 0.85 |
| 298540 / 2024-03-06 | true | true | clean_180D_window_old_profile_caveat_only | true, weight 0.95 |

Corporate-action notes:

- F&F has an old corporate-action candidate in 2022 only.
- 휠라홀딩스 has an old corporate-action candidate in 2018 only; 2024 row stream shows share-count drift after June, so the row is reduced weight.
- 더네이쳐홀딩스 has old corporate-action candidates in 2021 only.
- 081660 current/latest name is 미스토홀딩스 after 2025, but this research uses the 2024 name context, 휠라홀딩스.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| GLOBAL_BRAND_CHANNEL_INVENTORY_SELL_THROUGH_MARGIN_FAIL | C19 | brand/channel recovery beta without sell-through and OPM bridge is false-positive risk |
| GLOBAL_BRAND_INVENTORY_NORMALIZATION_MARGIN_BUFFER_STAGE2_WATCH | C19 | inventory normalization and margin buffer can prevent blanket 4C, but Green still needs revision/cash proof |
| LIFESTYLE_BRAND_GROWTH_INVENTORY_WITHOUT_SELL_THROUGH_MARGIN_BRIDGE | C19 | growth inventory without sell-through and cash conversion is false-positive risk |

## 7. Case Selection Summary

| case_id | symbol | company | role | polarity | why selected |
|---|---|---|---|---|---|
| C19_FNF_383220_2024_03_06_BRAND_CHINA_CHANNEL_INVENTORY_MARGIN_FALSE_RERATING | 383220 | F&F | failed_rerating | counterexample | mid MFE and large later MAE without sell-through/OPM bridge |
| C19_FILA_081660_2024_03_06_BRAND_INVENTORY_NORMALIZATION_MARGIN_BUFFER | 081660 | 휠라홀딩스 | inventory_margin_buffer | positive_boundary | limited MAE and modest MFE, useful as overblock guard |
| C19_NATURE_298540_2024_03_06_LIFESTYLE_BRAND_GROWTH_INVENTORY_SELL_THROUGH_FAIL | 298540 | 더네이쳐홀딩스 | failed_rerating | counterexample | low/mid MFE followed by severe 180D MAE |

## 8. Positive vs Counterexample Balance

| metric | count |
|---|---:|
| positive_boundary_case_count | 1 |
| counterexample_count | 2 |
| 4B_case_count | 2 |
| 4C_case_count | 2 |
| overblock_or_buffer_case_count | 1 |
| calibration_usable_case_count | 3 |
| calibration_usable_trigger_count | 3 |
| new_independent_case_count | 3 |
| reused_case_count | 0 |
| reduced_weight_caveat_count | 1 |

Minimum conditions pass.

## 9. Evidence Source Map

| case | source status | non-price evidence status | URL repair need |
|---|---|---|---|
| 383220 | source_proxy_only | channel/brand recovery beta but sell-through, inventory turn and OPM bridge absent | required; useful as counterexample |
| 081660 | source_proxy_only | inventory normalization and margin buffer partially visible | required before promotion |
| 298540 | source_proxy_only | lifestyle brand growth beta but sell-through, OPM and cash bridge absent | required; useful as counterexample |

Price-only evidence is not used to promote Stage3.

## 10. Price Data Source Map

| symbol | shard | profile |
|---|---|---|
| 383220 | atlas/ohlcv_tradable_by_symbol_year/383/383220/2024.csv | atlas/symbol_profiles/383/383220.json |
| 081660 | atlas/ohlcv_tradable_by_symbol_year/081/081660/2024.csv | atlas/symbol_profiles/081/081660.json |
| 298540 | atlas/ohlcv_tradable_by_symbol_year/298/298540/2024.csv | atlas/symbol_profiles/298/298540.json |

## 11. Case-by-Case Trigger Grid

| trigger_id | trigger_type | trigger_date | entry_date | entry_price | evidence summary |
|---|---|---:|---:|---:|---|
| FNF_383220_2024_03_06_STAGE2_FALSE_POSITIVE_CHANNEL_INVENTORY_MARGIN | Stage2 | 2024-03-06 | 2024-03-06 | 67700 | global brand/channel beta without sell-through/OPM bridge |
| FILA_081660_2024_03_06_STAGE2A_INVENTORY_NORMALIZATION_MARGIN_BUFFER | Stage2-Actionable | 2024-03-06 | 2024-03-06 | 39600 | inventory normalization and margin buffer |
| NATURE_298540_2024_03_06_STAGE2_FALSE_POSITIVE_GROWTH_INVENTORY | Stage2 | 2024-03-06 | 2024-03-06 | 14400 | growth inventory without sell-through/cash bridge |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 383220 | 2024-03-06 | 67700 | 14.33 | -8.86 | 14.33 | -14.77 | 14.33 | -27.18 | 2024-04-01 | 77400 | -36.30 |
| 081660 | 2024-03-06 | 39600 | 5.81 | -7.70 | 5.81 | -7.70 | 13.51 | -8.08 | 2024-09-25 | 44950 | -19.02 |
| 298540 | 2024-03-06 | 14400 | 9.86 | -10.07 | 11.74 | -20.42 | 11.74 | -38.19 | 2024-05-31 | 16090 | -44.69 |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely judgment | actual price-path verdict | stress result |
|---|---|---|---|
| 383220 | Stage2 risk if global brand recovery beta is over-credited | false positive | current_profile_false_positive |
| 081660 | hard 4C risk if all inventory risk is treated as stuffing | overblock / inventory-buffer case | current_profile_overblocks_if_inventory_normalization_buffer_ignored |
| 298540 | Stage2 risk if growth inventory is over-credited | false positive | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

No confirmed Stage3-Green trigger is used in this loop.

```text
green_lateness_ratio = not_applicable
reason = no_confirmed_Stage3_Green_trigger
```

C19 interpretation:

- Brand/channel recovery vocabulary can start Stage2-watch.
- Stage2A requires sell-through, inventory turn, OPM, receivable quality and cash conversion evidence.
- Inventory normalization can prevent blanket 4C, but it is still not Green without revision and cash bridge.
- Growth inventory without sell-through is a channel-stuffing risk.

## 15. 4B Local vs Full-window Timing Audit

| case | local peak proximity | full-window peak proximity | evidence type | verdict |
|---|---:|---:|---|---|
| 383220 | 0.87 | 1.00 | minor channel rebound / bridge absent | not Stage3 |
| 081660 | 0.88 | 1.00 | inventory normalization / margin buffer | Stage2-watch buffer, not Green |
| 298540 | 0.89 | 1.00 | growth inventory rebound / bridge absent | not Stage3 |

## 16. 4C Protection Audit

| case | four_c_protection_label | interpretation |
|---|---|---|
| 383220 | hard_4c_late | sell-through/OPM absence should have capped Stage2 earlier |
| 081660 | overblock_counterexample_watch | inventory normalization buffer should not be blanket 4C |
| 298540 | hard_4c_late | sell-through/cash bridge absence should have capped growth inventory earlier |

## 17. Sector-Specific Rule Candidate

```text
sector_specific_rule_candidate = true
scope = L5_CONSUMER_BRAND_RETAIL
confidence = medium
```

Candidate:

> In L5 consumer/brand/retail names, channel or brand recovery should promote Stage2A only when sell-through, inventory turns, OPM, receivable quality, revision and cash conversion are visible. Inventory normalization can remain Stage2-watch, but growth inventory without sell-through should route to 4C/watch.

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_rule_candidate = true
scope = C19_BRAND_RETAIL_INVENTORY_MARGIN
confidence = medium
```

Candidate C19 rule:

```text
C19_sell_through_inventory_margin_bridge_required =
  brand_or_retail_growth_route
  AND (sell_through_improvement OR inventory_turn_improvement OR OPM_bridge OR receivable_quality OR confirmed_revision OR cash_conversion)

if channel_growth_or_brand_recovery and inventory_margin_bridge_absent:
    cap_stage = Stage1/Stage2-watch
    do_not_allow_Stage3_Yellow_or_Green = true

if growth_inventory and sell_through_absent:
    add C19_channel_stuffing_guardrail = true

if inventory_normalization and margin_buffer and MAE_180D > -12:
    classify_as C19_inventory_normalization_buffer
    cap_stage = Stage2-watch_not_4C_not_Green

if share_count_drift_watch:
    reduce_independent_evidence_weight = true
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive / overblock | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_2_rolling_calibrated_proxy | current | 3 | 10.63 | -14.3 | 13.19 | -24.48 | 2 false positives + 1 overblock | C19 bridge too loose |
| P0b e2r_2_1_stock_web_calibrated | rollback | 3 | 10.63 | -14.3 | 13.19 | -24.48 | 2 false positives + 1 overblock | over-credits brand/channel beta |
| P1 sector_specific_candidate_profile | L5 | 1 buffer + 2 guard | 5.81 | -7.7 | 13.51 | -8.08 | 0 | better with sell-through/OPM bridge gate |
| P2 canonical_archetype_candidate_profile | C19 | 1 buffer + 2 guard | 5.81 | -7.7 | 13.51 | -8.08 | 0 | best shadow profile |
| P3 counterexample_guard_profile | C19 guard | 1 buffer + 2 guard | 5.81 | -7.7 | 13.51 | -8.08 | 0 | adds channel-stuffing and inventory buffer split |

## 20. Score-Return Alignment Matrix

| case | score-return alignment | current_profile_verdict |
|---|---|---|
| 383220 | Stage2 false positive if sell-through/OPM bridge not enforced | current_profile_false_positive |
| 081660 | inventory normalization buffer prevents blanket 4C | current_profile_overblocks_if_inventory_normalization_buffer_ignored |
| 298540 | Stage2 false positive if growth inventory is over-credited | current_profile_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive boundary | counterexample | 4B | 4C | new independent | reused | usable triggers | representative triggers | current errors | sector rule | canonical rule | coverage gap after loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L5_CONSUMER_BRAND_RETAIL | C19_BRAND_RETAIL_INVENTORY_MARGIN | mixed C19 fine ids | 1 | 2 | 2 | 2 | 3 | 0 | 3 | 3 | 3 | true | true | static 24 -> projected 27; still need 3 to reach 30 |

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
  - current_profile_overblocks_if_inventory_normalization_buffer_ignored
new_axis_proposed: C19_sell_through_inventory_margin_bridge_required|C19_channel_stuffing_guardrail|C19_inventory_normalization_buffer|share_count_drift_independent_weight_reduction
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: []
existing_axis_kept:
  - stage2_actionable_evidence_bonus
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
- Uses C19 Priority 0 coverage gap.
- Uses new local C19 symbols.
- Keeps 081660 with reduced independent weight because of 2024 share-count drift watch and post-2025 name change context.
- Treats 081660 as inventory normalization buffer, not Green promotion.
- Discards any repeated C02 loop138 materialization path.

Non-validation scope:

- Does not patch `stock_agent`.
- Does not change production scoring.
- Does not create a live watchlist.
- Does not claim verified URL evidence; evidence remains source-proxy and requires URL repair.
- Does not use price-only evidence to promote Stage3.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C19_sell_through_inventory_margin_bridge_required,canonical_archetype_specific,L5_CONSUMER_BRAND_RETAIL,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1,"383220/298540 show brand/channel growth beta can fail without sell-through, inventory turn, OPM and cash bridge while 081660 works only as Stage2 buffer","blocks two false positives while preserving inventory normalization buffer","FNF_383220_2024_03_06_STAGE2_FALSE_POSITIVE_CHANNEL_INVENTORY_MARGIN|FILA_081660_2024_03_06_STAGE2A_INVENTORY_NORMALIZATION_MARGIN_BUFFER|NATURE_298540_2024_03_06_STAGE2_FALSE_POSITIVE_GROWTH_INVENTORY",3,3,2,medium,canonical_shadow_only,"not production; URL repair required before promotion"
shadow_weight,C19_channel_stuffing_guardrail,canonical_archetype_specific,L5_CONSUMER_BRAND_RETAIL,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1,"298540 and 383220 had mid/low MFE followed by large MAE when sell-through and OPM bridge were absent","requires sell-through, inventory turn, receivable quality and OPM bridge before Stage2/Yellow promotion","FNF_383220_2024_03_06_STAGE2_FALSE_POSITIVE_CHANNEL_INVENTORY_MARGIN|NATURE_298540_2024_03_06_STAGE2_FALSE_POSITIVE_GROWTH_INVENTORY",2,2,2,medium,canonical_shadow_only,"false-positive guardrail"
shadow_weight,C19_inventory_normalization_buffer,canonical_archetype_specific,L5_CONSUMER_BRAND_RETAIL,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1,"081660 shows inventory normalization/margin buffer can prevent blanket hard 4C, although it should not become Green without revision/cash proof","keeps inventory normalization as Stage2-watch rather than hard 4C or Green","FILA_081660_2024_03_06_STAGE2A_INVENTORY_NORMALIZATION_MARGIN_BUFFER",1,1,0,medium,canonical_shadow_only,"overblock/buffer guard"
shadow_weight,share_count_drift_independent_weight_reduction,archetype_specific_quality_flag,L5_CONSUMER_BRAND_RETAIL,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1,"081660 shows 2024 share-count drift after selected entry and post-2025 name context","keeps row usable but lowers independent evidence weight","FILA_081660_2024_03_06_STAGE2A_INVENTORY_NORMALIZATION_MARGIN_BUFFER",1,1,0,medium,quality_shadow_only,"validation-quality guard"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"C19_FNF_383220_2024_03_06_BRAND_CHINA_CHANNEL_INVENTORY_MARGIN_FALSE_RERATING","symbol":"383220","company_name":"F&F","round":"R5","loop":"139","large_sector_id":"L5_CONSUMER_BRAND_RETAIL","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"GLOBAL_BRAND_CHANNEL_INVENTORY_SELL_THROUGH_MARGIN_FAIL","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"FNF_383220_2024_03_06_STAGE2_FALSE_POSITIVE_CHANNEL_INVENTORY_MARGIN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidate only in 2022; selected 2024 validation window is clean","independent_evidence_weight":0.95,"score_price_alignment":"global brand/channel recovery beta produced only a 14.33% 90D MFE and later -27.18% 180D MAE, so inventory/sell-through and margin bridge were required before Yellow/Green","current_profile_verdict":"current_profile_false_positive_if_brand_growth_overcredited_without_inventory_margin_bridge","price_source":"Songdaiki/stock-web","notes":"new local C19 symbol after C02 threshold completion; brand/channel inventory false-positive guard"}
{"row_type":"case","case_id":"C19_FILA_081660_2024_03_06_BRAND_INVENTORY_NORMALIZATION_MARGIN_BUFFER","symbol":"081660","company_name":"휠라홀딩스","round":"R5","loop":"139","large_sector_id":"L5_CONSUMER_BRAND_RETAIL","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"GLOBAL_BRAND_INVENTORY_NORMALIZATION_MARGIN_BUFFER_STAGE2_WATCH","case_type":"inventory_margin_buffer","positive_or_counterexample":"positive_boundary","best_trigger":"FILA_081660_2024_03_06_STAGE2A_INVENTORY_NORMALIZATION_MARGIN_BUFFER","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidate in 2018 only; selected 2024 window is clean, but 2024 share-count drift watch after June reduces weight","independent_evidence_weight":0.85,"score_price_alignment":"inventory normalization / brand margin buffer produced modest positive full-window MFE with limited MAE, so blanket 4C would overblock but Green still needed sell-through/revision confirmation","current_profile_verdict":"current_profile_overblocks_if_brand_inventory_normalization_treated_as_channel_stuffing","price_source":"Songdaiki/stock-web","notes":"current/latest name is 미스토홀딩스 after 2025; 2024 name context is 휠라홀딩스; reduced weight for share-count drift watch"}
{"row_type":"case","case_id":"C19_NATURE_298540_2024_03_06_LIFESTYLE_BRAND_GROWTH_INVENTORY_SELL_THROUGH_FAIL","symbol":"298540","company_name":"더네이쳐홀딩스","round":"R5","loop":"139","large_sector_id":"L5_CONSUMER_BRAND_RETAIL","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"LIFESTYLE_BRAND_GROWTH_INVENTORY_WITHOUT_SELL_THROUGH_MARGIN_BRIDGE","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"NATURE_298540_2024_03_06_STAGE2_FALSE_POSITIVE_GROWTH_INVENTORY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":"old corporate-action candidates only in 2021; selected 2024 window is clean","independent_evidence_weight":0.95,"score_price_alignment":"lifestyle brand growth/inventory beta produced only 11.74% 90D MFE and then -38.19% 180D MAE, confirming sell-through/OPM bridge as mandatory","current_profile_verdict":"current_profile_false_positive_if_growth_inventory_overcredited_without_sell_through","price_source":"Songdaiki/stock-web","notes":"clean 2024 validation window; strong C19 sell-through counterexample"}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"FNF_383220_2024_03_06_STAGE2_FALSE_POSITIVE_CHANNEL_INVENTORY_MARGIN","case_id":"C19_FNF_383220_2024_03_06_BRAND_CHINA_CHANNEL_INVENTORY_MARGIN_FALSE_RERATING","symbol":"383220","company_name":"F&F","round":"R5","loop":"139","large_sector_id":"L5_CONSUMER_BRAND_RETAIL","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"GLOBAL_BRAND_CHANNEL_INVENTORY_SELL_THROUGH_MARGIN_FAIL","sector":"consumer / brand / retail","primary_archetype":"brand_retail_inventory_margin","loop_objective":"coverage_gap_fill|counterexample_mining|inventory_sell_through_margin_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":67700.0,"evidence_available_at_that_date":"source_proxy_only: global brand/channel recovery, China channel narrative and brand beta visible, but inventory quality, sell-through, OPM and receivable-to-cash bridge not confirmed; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["global_brand_recovery_beta","channel_recovery_narrative","relative_strength_partial"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["minor_channel_rebound","bridge_absent","full_window_drawdown"],"stage4c_evidence_fields":["inventory_quality_absent","sell_through_absent","OPM_bridge_absent","receivable_cash_bridge_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/383/383220/2024.csv","profile_path":"atlas/symbol_profiles/383/383220.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":14.33,"MFE_90D_pct":14.33,"MFE_180D_pct":14.33,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-8.86,"MAE_90D_pct":-14.77,"MAE_180D_pct":-27.18,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-04-01","peak_price":77400.0,"drawdown_after_peak_pct":-36.3,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.87,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"brand/channel rebound could not become C19 Stage3 without sell-through, inventory-quality and OPM bridge","four_b_evidence_type":["minor_rebound","bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_mid_mfe_later_mae_bridge_absent","current_profile_verdict":"current_profile_false_positive_if_brand_growth_overcredited_without_inventory_margin_bridge","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C19_383220_2024_03_06_67700","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidate before selected window","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"FILA_081660_2024_03_06_STAGE2A_INVENTORY_NORMALIZATION_MARGIN_BUFFER","case_id":"C19_FILA_081660_2024_03_06_BRAND_INVENTORY_NORMALIZATION_MARGIN_BUFFER","symbol":"081660","company_name":"휠라홀딩스","round":"R5","loop":"139","large_sector_id":"L5_CONSUMER_BRAND_RETAIL","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"GLOBAL_BRAND_INVENTORY_NORMALIZATION_MARGIN_BUFFER_STAGE2_WATCH","sector":"consumer / brand / retail","primary_archetype":"brand_retail_inventory_margin","loop_objective":"coverage_gap_fill|counterexample_mining|inventory_sell_through_margin_stress_test|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":39600.0,"evidence_available_at_that_date":"source_proxy_only: global brand inventory normalization, margin buffer, channel cleanup and steady cash-return narrative visible; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["inventory_normalization","margin_buffer","global_brand_channel_cleanup","relative_strength_stability"],"stage3_evidence_fields":["sell_through_partial","OPM_bridge_partial","revision_bridge_pending","cash_conversion_pending"],"stage4b_evidence_fields":["inventory_normalization_rerating_watch","valuation_peak_watch","share_count_drift_watch"],"stage4c_evidence_fields":["inventory_reaccumulation_watch"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/081/081660/2024.csv","profile_path":"atlas/symbol_profiles/081/081660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":5.81,"MFE_90D_pct":5.81,"MFE_180D_pct":13.51,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-7.7,"MAE_90D_pct":-7.7,"MAE_180D_pct":-8.08,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-09-25","peak_price":44950.0,"drawdown_after_peak_pct":-19.02,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.88,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"inventory normalization buffer prevented blanket 4C, but Stage3/Green still needs sell-through, OPM and revision confirmation","four_b_evidence_type":["inventory_normalization","margin_buffer"],"four_c_protection_label":"overblock_counterexample_watch","trigger_outcome_label":"positive_boundary_inventory_margin_buffer","current_profile_verdict":"current_profile_overblocks_if_brand_inventory_normalization_treated_as_channel_stuffing","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":["share_count_drift_after_june_reduced_weight"],"corporate_action_window_status":"clean_entry_window_old_profile_caveat_but_2024_share_count_drift_watch","same_entry_group_id":"C19_081660_2024_03_06_39600","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidate before selected window; share-count drift after June","independent_evidence_weight":0.85,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"NATURE_298540_2024_03_06_STAGE2_FALSE_POSITIVE_GROWTH_INVENTORY","case_id":"C19_NATURE_298540_2024_03_06_LIFESTYLE_BRAND_GROWTH_INVENTORY_SELL_THROUGH_FAIL","symbol":"298540","company_name":"더네이쳐홀딩스","round":"R5","loop":"139","large_sector_id":"L5_CONSUMER_BRAND_RETAIL","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","fine_archetype_id":"LIFESTYLE_BRAND_GROWTH_INVENTORY_WITHOUT_SELL_THROUGH_MARGIN_BRIDGE","sector":"consumer / brand / retail","primary_archetype":"brand_retail_inventory_margin","loop_objective":"coverage_gap_fill|counterexample_mining|inventory_sell_through_margin_stress_test|canonical_archetype_compression","trigger_type":"Stage2","trigger_date":"2024-03-06","entry_date":"2024-03-06","entry_price":14400.0,"evidence_available_at_that_date":"source_proxy_only: lifestyle brand growth and offline/channel expansion narrative visible, but sell-through, inventory turn, OPM and cash conversion bridge absent; verified URL repair pending","evidence_source":"source_proxy_only_not_price_only","stage2_evidence_fields":["lifestyle_brand_growth_beta","channel_expansion_narrative","relative_strength_partial"],"stage3_evidence_fields":["none_confirmed"],"stage4b_evidence_fields":["temporary_growth_rebound","bridge_absent"],"stage4c_evidence_fields":["sell_through_absent","inventory_turn_absent","OPM_bridge_absent","cash_conversion_absent"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/298/298540/2024.csv","profile_path":"atlas/symbol_profiles/298/298540.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":9.86,"MFE_90D_pct":11.74,"MFE_180D_pct":11.74,"MFE_1Y_pct":"unavailable_not_needed_for_delta","MFE_2Y_pct":"insufficient_forward_window_or_not_computed","MAE_30D_pct":-10.07,"MAE_90D_pct":-20.42,"MAE_180D_pct":-38.19,"MAE_1Y_pct":"unavailable_not_needed_for_delta","below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-31","peak_price":16090.0,"drawdown_after_peak_pct":-44.69,"green_lateness_ratio":"not_applicable_no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.89,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"growth inventory rebound did not become Stage3 without sell-through, inventory-turn and OPM bridge","four_b_evidence_type":["temporary_growth_rebound","bridge_absent"],"four_c_protection_label":"hard_4c_late","trigger_outcome_label":"counterexample_low_mid_mfe_high_mae_bridge_absent","current_profile_verdict":"current_profile_false_positive_if_growth_inventory_overcredited_without_sell_through","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_old_profile_caveat_only","same_entry_group_id":"C19_298540_2024_03_06_14400","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":"old corporate-action candidates before selected window","independent_evidence_weight":0.95,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C19_FNF_383220_2024_03_06_BRAND_CHINA_CHANNEL_INVENTORY_MARGIN_FALSE_RERATING","trigger_id":"FNF_383220_2024_03_06_STAGE2_FALSE_POSITIVE_CHANNEL_INVENTORY_MARGIN","symbol":"383220","large_sector_id":"L5_CONSUMER_BRAND_RETAIL","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":2,"revision_score":1,"relative_strength_score":4,"customer_quality_score":4,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":58,"stage_label_before":"Stage2 false-positive / brand channel recovery risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":2,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":43,"stage_label_after":"Stage1/4C-watch, not C19 Yellow","changed_components":["backlog_visibility_score","margin_bridge_score","revision_score","relative_strength_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Brand/channel beta lacked sell-through, inventory turn, OPM and cash-conversion bridge.","MFE_90D_pct":14.33,"MAE_90D_pct":-14.77,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive_if_brand_growth_overcredited_without_inventory_margin_bridge"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C19_FILA_081660_2024_03_06_BRAND_INVENTORY_NORMALIZATION_MARGIN_BUFFER","trigger_id":"FILA_081660_2024_03_06_STAGE2A_INVENTORY_NORMALIZATION_MARGIN_BUFFER","symbol":"081660","large_sector_id":"L5_CONSUMER_BRAND_RETAIL","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":1,"accounting_trust_risk_score":0},"weighted_score_before":65,"stage_label_before":"Stage2-watch / inventory normalization buffer","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":4,"revision_score":3,"relative_strength_score":4,"customer_quality_score":5,"policy_or_regulatory_score":0,"valuation_repricing_score":2,"execution_risk_score":6,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":2,"accounting_trust_risk_score":0},"weighted_score_after":61,"stage_label_after":"Stage2-watch with C19 inventory buffer, not Green","changed_components":["valuation_repricing_score","execution_risk_score","dilution_cb_risk_score"],"component_delta_explanation":"Inventory normalization buffer prevents blanket 4C, but Green requires sell-through, OPM and revision proof.","MFE_90D_pct":5.81,"MAE_90D_pct":-7.7,"score_return_alignment_label":"inventory_margin_buffer_overblock_guard","current_profile_verdict":"current_profile_overblocks_if_brand_inventory_normalization_treated_as_channel_stuffing"}
{"row_type":"score_simulation","profile_id":"e2r_2_2_rolling_calibrated_proxy","case_id":"C19_NATURE_298540_2024_03_06_LIFESTYLE_BRAND_GROWTH_INVENTORY_SELL_THROUGH_FAIL","trigger_id":"NATURE_298540_2024_03_06_STAGE2_FALSE_POSITIVE_GROWTH_INVENTORY","symbol":"298540","large_sector_id":"L5_CONSUMER_BRAND_RETAIL","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":1,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":4,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":4,"execution_risk_score":7,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":56,"stage_label_before":"Stage2 false-positive / growth inventory risk","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":1,"customer_quality_score":2,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":41,"stage_label_after":"Stage1/4C-watch, not C19 Stage2","changed_components":["backlog_visibility_score","margin_bridge_score","relative_strength_score","customer_quality_score","valuation_repricing_score","execution_risk_score"],"component_delta_explanation":"Growth inventory did not convert into sell-through, OPM or cash conversion.","MFE_90D_pct":11.74,"MAE_90D_pct":-20.42,"score_return_alignment_label":"false_positive_guard_needed","current_profile_verdict":"current_profile_false_positive_if_growth_inventory_overcredited_without_sell_through"}
```

### 25.5 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R5","loop":"139","large_sector_id":"L5_CONSUMER_BRAND_RETAIL","canonical_archetype_id":"C19_BRAND_RETAIL_INVENTORY_MARGIN","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["current_profile_false_positive","current_profile_overblocks_if_inventory_normalization_buffer_ignored"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R5
completed_loop = 139
selection_basis = docs/core/V12_Research_No_Repeat_Index.md + local generated loop memory
selected_priority_bucket = Priority 0
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
next_recommended_archetypes = C19_BRAND_RETAIL_INVENTORY_MARGIN, C27_CONTENT_IP_GLOBAL_MONETIZATION, C24_BIO_TRIAL_DATA_EVENT_RISK, C28_SOFTWARE_SECURITY_CONTRACT_RETENTION, C19_BRAND_RETAIL_INVENTORY_MARGIN_ONLY_IF_UNCOVERED_FINE_ARCHETYPE
```

If this loop is accepted, C19 moves to projected 27 rows and still needs 3 rows to reach the 30-row minimum stability threshold. The next run should re-read the latest No-Repeat Index and avoid repeating these C19 symbol/trigger/date combinations.

## 28. Source Notes

- Main execution procedure: docs/core/e2r_v12_prompt_round_scheduler_corrected.txt.
- Duplicate avoidance ledger: docs/core/V12_Research_No_Repeat_Index.md.
- Price atlas: Songdaiki/stock-web.
- Price files used:
  - atlas/ohlcv_tradable_by_symbol_year/383/383220/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/081/081660/2024.csv
  - atlas/ohlcv_tradable_by_symbol_year/298/298540/2024.csv
- Symbol profiles used:
  - atlas/symbol_profiles/383/383220.json
  - atlas/symbol_profiles/081/081660.json
  - atlas/symbol_profiles/298/298540.json
- Discarded duplicate attempt:
  - e2r_stock_web_v12_residual_round_R1_loop_138_L1_INFRA_DEFENSE_GRID_C02_POWER_GRID_DATACENTER_CAPEX_research.md
- Evidence URL status: `source_proxy_only`, `evidence_url_pending`.
