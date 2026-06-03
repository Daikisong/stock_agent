# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session: post_calibrated_sector_archetype_residual_research
scheduled_round: R4
scheduled_loop: 74
completed_round: R4
completed_loop: 74
large_sector_id: L4_MATERIALS_SPREAD_RESOURCE
canonical_archetype_id: C15_MATERIAL_SPREAD_SUPERCYCLE
fine_archetype_id: COPPER_SPREAD_PRODUCER_CONVERSION_VS_PRICE_PROXY
output_file: e2r_stock_web_v12_residual_round_R4_loop_74_L4_MATERIALS_SPREAD_RESOURCE_C15_MATERIAL_SPREAD_SUPERCYCLE_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_web_price_atlas_access_required: true
```

This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R4/L4_MATERIALS_SPREAD_RESOURCE/C15_MATERIAL_SPREAD_SUPERCYCLE.

## 1. Current Calibrated Profile Assumption

- current_default_profile_proxy: `e2r_2_1_stock_web_calibrated`
- rollback_reference_profile_id: `e2r_2_0_baseline_reference`
- existing axes treated as already applied: `stage2_actionable_evidence_bonus`, `stage3_yellow_total_min`, `stage3_green_total_min`, `stage3_green_revision_min`, `stage3_cross_evidence_green_buffer`, `price_only_blowoff_blocks_positive_stage`, `full_4b_requires_non_price_evidence`, `hard_4c_thesis_break_routes_to_4c`.
- Existing-axis status: `existing_axis_tested`, `existing_axis_strengthened`; no production change.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R4 |
| scheduled_loop | 74 |
| required_large_sector_id | L4_MATERIALS_SPREAD_RESOURCE |
| selected_canonical_archetype_id | C15_MATERIAL_SPREAD_SUPERCYCLE |
| round_sector_consistency | pass |
| loop_objective | sector_specific_rule_discovery, canonical_archetype_compression, counterexample_mining, 4B_non_price_requirement_stress_test |

## 3. Previous Coverage / Duplicate Avoidance Check

The no-repeat index shows C15 has moderate coverage but still has few bad Stage2 rows relative to C17 and no 4C rows in the C15 row. The top repeated C15 symbols are `005490`, `004020`, `001430`, `018470`, `001230`, `011170`; this loop avoided those symbols and selected `103140`, `025820`, and `012800`. Hard duplicate key tested conceptually: `canonical_archetype_id + symbol + trigger_type + entry_date`.

| duplicate gate | result |
|---|---|
| same canonical allowed | yes |
| repeated top C15 symbols avoided | yes |
| new_symbol_count | 3 |
| new_trigger_family_count | 3 |
| reused_case_count | 0 |
| schema_rematerialization_only | false |

## 4. Stock-Web OHLC Input / Price Source Validation

| manifest field | value |
|---|---|
| source_name | `FinanceData/marcap` |
| source_repo_url | `https://github.com/FinanceData/marcap` |
| price_adjustment_status | `raw_unadjusted_marcap` |
| min_date | `1995-05-02` |
| max_date | `2026-02-20` |
| tradable_row_count | `14354401` |
| raw_row_count | `15214118` |
| symbol_count | `5414` |
| active_like_symbol_count | `2868` |
| inactive_or_delisted_like_symbol_count | `2546` |
| markets | `['KONEX', 'KOSDAQ', 'KOSDAQ GLOBAL', 'KOSPI']` |
| calibration_shard_root | `atlas/ohlcv_tradable_by_symbol_year` |
| raw_shard_root | `atlas/ohlcv_raw_by_symbol_year` |
| schema_path | `atlas/schema.json` |
| universe_path | `atlas/universe/all_symbols.csv` |

Schema basis: tradable shards use `d,o,h,l,c,v,a,mc,s,m`; raw shards add `rs`. MFE/MAE use max high / min low over tradable rows. Corporate-action windows are blocked by default.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry row exists | >=180 forward tradable days | corporate_action_window_status | calibration_usable |
|---|---:|---|---|---|---|---|
| R4L74_C15_103140_20240222_COPPER_DEFENSE_MARGIN_BRIDGE | 103140 | 2024-02-22 | true | true | clean_180D_window | true |
| R4L74_C15_025820_20240404_COPPER_PROXY_PRICE_ONLY_SPIKE | 025820 | 2024-04-04 | true | true | clean_180D_window; historical corporate candidates exist outside window | true |
| R4L74_C15_012800_20240404_COPPER_PROXY_SMALLCAP_SPIKE | 012800 | 2024-04-04 | true | true | clean_180D_window; historical corporate candidates exist outside window | true |

Historical corporate-action candidates for `025820` and `012800` exist only far outside the 2024 trigger windows, so the 180D windows remain calibration-usable. `103140` has no corporate-action candidate dates in the profile used here.

## 6. Canonical Archetype Compression Map

| fine_archetype | canonical_archetype_id | compression logic |
|---|---|---|
| COPPER_SPREAD_PRODUCER_CONVERSION_VS_PRICE_PROXY | C15_MATERIAL_SPREAD_SUPERCYCLE | Separates commodity spread tailwind into company-level producer conversion versus price-beta proxy. |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger_family | current_profile_verdict |
|---|---:|---|---|---|---|
| R4L74_C15_103140_20240222_COPPER_DEFENSE_MARGIN_BRIDGE | 103140 | 풍산 | structural_success | producer_margin_bridge_with_nonferrous_price_and_defense_order_visibility | current_profile_correct |
| R4L74_C15_025820_20240404_COPPER_PROXY_PRICE_ONLY_SPIKE | 025820 | 이구산업 | price_moved_without_evidence | copper_price_proxy_without_company_specific_conversion | current_profile_false_positive |
| R4L74_C15_012800_20240404_COPPER_PROXY_SMALLCAP_SPIKE | 012800 | 대창 | failed_rerating | smallcap_copper_beta_without_margin_bridge | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

| positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | calibration_usable_case_count |
|---:|---:|---:|---:|---:|
| 1 | 2 | 3 | 2 | 3 |

The balance is intentionally counterexample-heavy because R4/C15 already has many successful spread rerating cases but fewer proxy-failure rows. The positive case provides the anchor: spread tailwind mattered only when it came with producer-level conversion.

## 9. Evidence Source Map

| trigger_id | evidence_source | stage2_fields | stage3_fields | 4B_fields | 4C_fields |
|---|---|---|---|---|---|
| R4L74_C15_103140_STAGE2A_20240222 | historical public-event proxy: 2024 copper-price upcycle + defense export/order visibility + stock-web price reaction; source_url_pending=false for price rows, evidence_url_pending=true | `public_event_or_disclosure,relative_strength,capacity_or_volume_route,backlog_or_delivery_visibility,early_revision_signal` | `confirmed_revision,margin_bridge,financial_visibility,durable_customer_confirmation,low_red_team_risk` | `valuation_blowoff,positioning_overheat,margin_or_backlog_slowdown` | `` |
| R4L74_C15_025820_STAGE2_FP_20240404 | historical public-event proxy: copper price breakout / thematic copper proxy rally + stock-web price rows; no company-level conversion evidence used | `relative_strength,policy_or_regulatory_optionality` | `` | `price_only_local_peak,valuation_blowoff,positioning_overheat` | `thesis_evidence_broken` |
| R4L74_C15_012800_STAGE2_FP_20240404 | historical public-event proxy: copper thematic rally + stock-web price rows; company-specific margin evidence not used | `relative_strength,policy_or_regulatory_optionality` | `` | `price_only_local_peak,valuation_blowoff,positioning_overheat` | `thesis_evidence_broken` |

## 10. Price Data Source Map

| symbol | company | profile_path | price_shard_path | price_basis | adjustment |
|---:|---|---|---|---|---|
| 103140 | 풍산 | `atlas/symbol_profiles/103/103140.json` | `atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv` | tradable_raw | raw_unadjusted_marcap |
| 025820 | 이구산업 | `atlas/symbol_profiles/025/025820.json` | `atlas/ohlcv_tradable_by_symbol_year/025/025820/2024.csv` | tradable_raw | raw_unadjusted_marcap |
| 012800 | 대창 | `atlas/symbol_profiles/012/012800.json` | `atlas/ohlcv_tradable_by_symbol_year/012/012800/2024.csv` | tradable_raw | raw_unadjusted_marcap |

## 11. Case-by-Case Trigger Grid

| trigger_id | type | entry | score_before -> after | label_before -> after | outcome |
|---|---|---:|---:|---|---|
| R4L74_C15_103140_STAGE2A_20240222 | Stage2-Actionable | 2024-02-22 / 42200 | 78 -> 82 | Stage3-Yellow -> Stage3-Yellow / Stage2-Actionable-confirmed | structural_success_high_mfe_with_order_margin_bridge |
| R4L74_C15_025820_STAGE2_FP_20240404 | Stage2-FalsePositive | 2024-04-04 / 5430 | 76 -> 64 | Stage3-Yellow / false Stage2-Actionable -> Stage2-Watch / blocked_positive_stage | false_positive_high_mfe_high_mae_roundtrip |
| R4L74_C15_012800_STAGE2_FP_20240404 | Stage2-FalsePositive | 2024-04-04 / 1470 | 75 -> 62 | Stage3-Yellow / false Stage2-Actionable -> Stage2-Watch / blocked_positive_stage | false_positive_price_proxy_roundtrip |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry_price | MFE_30D | MAE_30D | MFE_90D | MAE_90D | MFE_180D | MAE_180D | peak_date | peak_price | drawdown_after_peak | below_entry_30D | below_entry_90D |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---|---|
| R4L74_C15_103140_STAGE2A_20240222 | 42200 | 26.07% | -7.70% | 86.97% | -7.70% | 86.97% | -7.70% | 2024-05-14 | 78900 | -40.43% | true | true |
| R4L74_C15_025820_STAGE2_FP_20240404 | 5430 | 55.06% | -11.14% | 55.06% | -30.11% | 55.06% | -30.11% | 2024-05-20 | 8420 | -54.93% | false | true |
| R4L74_C15_012800_STAGE2_FP_20240404 | 1470 | 57.82% | -4.76% | 57.82% | -25.17% | 57.82% | -25.17% | 2024-05-21 | 2320 | -52.59% | true | true |

## 13. Current Calibrated Profile Stress Test

| case | current_profile_judgment | fit_to_MFE_MAE | Stage2 bonus | Yellow 75 | Green 87/rev55 | price-only guard | full 4B non-price requirement | hard 4C routing | verdict |
|---|---|---|---|---|---|---|---|---|---|
| 103140 | promote as actionable once spread + order/margin bridge appears | correct: 86.97% MFE90 / -7.70% MAE90 | adequate | not too loose | Green somewhat late but not peak-only | appropriate | appropriate | watch-only until non-price 4B | current_profile_correct |
| 025820 | may over-promote if copper price proxy is treated as company evidence | false positive: 55.06% MFE but -30.11% MAE and -54.93% drawdown after peak | too generous if proxy-only | too loose | no real Green | existing guard needs C15-specific conversion test | price-only local peak should not be full 4B | 4C after conversion failure useful | current_profile_false_positive |
| 012800 | may over-promote if smallcap copper beta is treated as spread supercycle | false positive: 57.82% MFE but -25.17% MAE and -52.59% drawdown | too generous if proxy-only | too loose | no real Green | existing guard needs C15-specific conversion test | price-only local peak should not be full 4B | 4C after theme fade useful | current_profile_false_positive |

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | Yellow/Green comparison | green_lateness_ratio | interpretation |
|---|---|---|---|---|
| 103140 | 2024-02-22 @ 42,200 | Later Green confirmation would still catch upside but after large early move | 0.32 | Green somewhat late; Stage2 Actionable useful when non-price bridge exists. |
| 025820 | 2024-04-04 @ 5,430 | No confirmed Green should be allowed; price-only MFE is tradable but not thesis-grade | not_applicable | Treat as proxy watch / 4B overlay, not positive Stage2. |
| 012800 | 2024-04-04 @ 1,470 | No confirmed Green should be allowed; roundtrip confirms missing evidence | not_applicable | Treat as proxy watch / 4B overlay, not positive Stage2. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | four_b_local_peak_proximity | four_b_full_window_peak_proximity | evidence_type | verdict |
|---|---:|---:|---|---|
| R4L74_C15_103140_STAGE2A_20240222 | 0.815 | 0.815 | `valuation_blowoff,positioning_overheat,revision_slowdown` | good_full_window_4B_timing |
| R4L74_C15_025820_STAGE2_FP_20240404 | 0.819 | 0.819 | `price_only,valuation_blowoff,positioning_overheat` | price_only_local_4B_watch_not_full_4B |
| R4L74_C15_012800_STAGE2_FP_20240404 | 0.829 | 0.829 | `price_only,valuation_blowoff,positioning_overheat` | price_only_local_4B_watch_not_full_4B |

## 16. 4C Protection Audit

| case | four_c_protection_label | comment |
|---|---|---|
| 103140 | thesis_break_watch_only | No hard 4C; producer thesis remained alive, but valuation/revision slowdown could shift to 4B overlay. |
| 025820 | hard_4c_success_after_no_conversion | After proxy peak, the absence of company-level margin/revision bridge gave a clean thesis-break route. |
| 012800 | hard_4c_success_after_theme_fade | The theme faded without confirmed earnings conversion; 4C would protect against post-peak drawdown. |

## 17. Sector-Specific Rule Candidate

`sector_specific_rule_candidate = true`

For L4 materials, commodity-price evidence should be treated like weather over a field: it can help the crop grow, but it is not the crop. The Stage2 promotion gate should require evidence that the price tailwind actually enters the company P&L through producer inventory, realized ASP, margin bridge, order conversion, or revision. Without this bridge, the row should be capped at `Stage2-Watch` and routed to a 4B/4C guard after a local peak.

Proposed shadow rule:

```text
if large_sector_id == L4_MATERIALS_SPREAD_RESOURCE and canonical_archetype_id == C15_MATERIAL_SPREAD_SUPERCYCLE:
    if commodity_price_or_relative_strength_only and producer_conversion_evidence_family_count < 2:
        cap_positive_stage = Stage2-Watch
        block_stage3_green = true
        allow_4b_overlay = price_only_local_peak_watch
    if producer_conversion_evidence_family_count >= 2 and margin_bridge_score >= 6:
        allow_stage2_actionable = true
        add_c15_producer_conversion_bridge_bonus = +3
```

## 18. Canonical-Archetype Rule Candidate

`canonical_archetype_rule_candidate = true`

For C15, compress copper, steel, chemical, and resource spreads into one evidence rule: spread is only thesis-grade when it is converted into company economics. The proxy-only versions can have high MFE, but the backtest shows high MAE and large post-peak drawdowns; they belong to watch/overlay logic, not positive-stage promotion.

## 19. Before / After Backtest Comparison

| profile_id | selected cases | avg_MFE_90D | avg_MAE_90D | false_positive_rate | score_return_alignment |
|---|---:|---:|---:|---:|---|
| P0 current proxy | 3 | 66.62% | -20.99% | 0.67 | mixed |
| P1 sector-specific candidate | 1 promoted / 2 blocked | 86.97% on promoted case | -7.70% on promoted case | 0.00 | better precision |
| P2 canonical candidate | 1 promoted / 2 blocked | 86.97% on promoted case | -7.70% on promoted case | 0.00 | better precision |
| P3 counterexample guard | 2 blocked | n/a | avoids -27.64% avg MAE on proxy rows | 0.00 | improves guardrail |

## 20. Score-Return Alignment Matrix

| trigger_id | score_before | score_after | MFE_90D | MAE_90D | alignment_after |
|---|---:|---:|---:|---:|---|
| R4L74_C15_103140_STAGE2A_20240222 | 78 | 82 | 86.97% | -7.70% | aligned |
| R4L74_C15_025820_STAGE2_FP_20240404 | 76 | 64 | 55.06% | -30.11% | guarded_false_positive |
| R4L74_C15_012800_STAGE2_FP_20240404 | 75 | 62 | 57.82% | -25.17% | guarded_false_positive |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L4_MATERIALS_SPREAD_RESOURCE | C15_MATERIAL_SPREAD_SUPERCYCLE | COPPER_SPREAD_PRODUCER_CONVERSION_VS_PRICE_PROXY | 1 | 2 | 3 | 2 | 3 | 0 | 3 | 3 | 2 | true | true | C15 now has explicit copper-proxy false-positive rows; still needs steel/chemical holdout. |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - commodity_price_proxy_false_positive
  - local_peak_watch_should_not_be_full_4B
new_axis_proposed:
  - c15_price_proxy_positive_stage_cap
  - c15_producer_conversion_bridge_bonus
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: []
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated scope: stock-web tradable_raw OHLC rows, 180D MFE/MAE, profile-level corporate-action window checks, duplicate-avoidance against no-repeat coverage summary, and shadow-only score simulation. Non-validation scope: this file does not alter production scoring, does not inspect `stock_agent/src`, does not create live candidates, and does not make investment recommendations. Evidence text is historical proxy classification; future batch implementation should replace evidence_url_pending rows with exact disclosure/report URLs when available.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c15_price_proxy_positive_stage_cap,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,none,Stage2-Watch,cap,"Copper price beta without company conversion produced high MFE but high MAE and roundtrip risk","false_positive_rate 0.67 -> 0.00 in sample; avg MAE selected cases improves by excluding proxy false positives","R4L74_C15_025820_STAGE2_FP_20240404|R4L74_C15_012800_STAGE2_FP_20240404",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c15_producer_conversion_bridge_bonus,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,+3,+3,"Producer-level margin/revision/order evidence separated 풍산 from copper-beta proxies","retains structural success 103140 while blocking two false positives","R4L74_C15_103140_STAGE2A_20240222",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R4L74_C15_103140_20240222_COPPER_DEFENSE_MARGIN_BRIDGE","symbol":"103140","company_name":"풍산","round":"R4","loop":"74","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_SPREAD_PRODUCER_CONVERSION_VS_PRICE_PROXY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R4L74_C15_103140_STAGE2A_20240222","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Copper spread tailwind plus defense/ammunition export visibility; producer-level margin bridge visible before full rerating."}
{"row_type":"case","case_id":"R4L74_C15_025820_20240404_COPPER_PROXY_PRICE_ONLY_SPIKE","symbol":"025820","company_name":"이구산업","round":"R4","loop":"74","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_SPREAD_PRODUCER_CONVERSION_VS_PRICE_PROXY","case_type":"price_moved_without_evidence","positive_or_counterexample":"counterexample","best_trigger":"R4L74_C15_025820_STAGE2_FP_20240404","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_high_mfe_high_drawdown","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Copper-price proxy and volume spike were visible, but company-specific realized spread, customer conversion, and durable margin bridge were not confirmed at trigger date."}
{"row_type":"case","case_id":"R4L74_C15_012800_20240404_COPPER_PROXY_SMALLCAP_SPIKE","symbol":"012800","company_name":"대창","round":"R4","loop":"74","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_SPREAD_PRODUCER_CONVERSION_VS_PRICE_PROXY","case_type":"failed_rerating","positive_or_counterexample":"counterexample","best_trigger":"R4L74_C15_012800_STAGE2_FP_20240404","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"false_positive_high_mfe_high_drawdown","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Copper beta and small-cap thematic flow were visible, but no durable margin bridge, no customer-quality evidence, and no confirmed revision path were available at trigger date."}
```

### 25.3 trigger rows

```jsonl
{"row_type":"trigger","trigger_id":"R4L74_C15_103140_STAGE2A_20240222","case_id":"R4L74_C15_103140_20240222_COPPER_DEFENSE_MARGIN_BRIDGE","symbol":"103140","company_name":"풍산","round":"R4","loop":"74","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_SPREAD_PRODUCER_CONVERSION_VS_PRICE_PROXY","sector":"materials_nonferrous_copper","primary_archetype":"material_spread_supercycle","loop_objective":"sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-22","evidence_available_at_that_date":"Copper spread tailwind plus defense/ammunition export visibility; producer-level margin bridge visible before full rerating.","evidence_source":"historical public-event proxy: 2024 copper-price upcycle + defense export/order visibility + stock-web price reaction; source_url_pending=false for price rows, evidence_url_pending=true","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","capacity_or_volume_route","backlog_or_delivery_visibility","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","financial_visibility","durable_customer_confirmation","low_red_team_risk"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","margin_or_backlog_slowdown"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv","profile_path":"atlas/symbol_profiles/103/103140.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-22","entry_price":42200,"MFE_30D_pct":26.07,"MFE_90D_pct":86.97,"MFE_180D_pct":86.97,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.7,"MAE_90D_pct":-7.7,"MAE_180D_pct":-7.7,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-14","peak_price":78900,"drawdown_after_peak_pct":-40.43,"green_lateness_ratio":0.32,"four_b_local_peak_proximity":0.815,"four_b_full_window_peak_proximity":0.815,"four_b_timing_verdict":"good_full_window_4B_timing","four_b_evidence_type":["valuation_blowoff","positioning_overheat","revision_slowdown"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_success_high_mfe_with_order_margin_bridge","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R4L74_C15_103140_20240222_COPPER_DEFENSE_MARGIN_BRIDGE::2024-02-22","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L74_C15_025820_STAGE2_FP_20240404","case_id":"R4L74_C15_025820_20240404_COPPER_PROXY_PRICE_ONLY_SPIKE","symbol":"025820","company_name":"이구산업","round":"R4","loop":"74","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_SPREAD_PRODUCER_CONVERSION_VS_PRICE_PROXY","sector":"materials_nonferrous_copper","primary_archetype":"material_spread_supercycle","loop_objective":"sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive","trigger_date":"2024-04-04","evidence_available_at_that_date":"Copper-price proxy and volume spike were visible, but company-specific realized spread, customer conversion, and durable margin bridge were not confirmed at trigger date.","evidence_source":"historical public-event proxy: copper price breakout / thematic copper proxy rally + stock-web price rows; no company-level conversion evidence used","stage2_evidence_fields":["relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/025/025820/2024.csv","profile_path":"atlas/symbol_profiles/025/025820.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-04","entry_price":5430,"MFE_30D_pct":55.06,"MFE_90D_pct":55.06,"MFE_180D_pct":55.06,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-11.14,"MAE_90D_pct":-30.11,"MAE_180D_pct":-30.11,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":true,"peak_date":"2024-05-20","peak_price":8420,"drawdown_after_peak_pct":-54.93,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.819,"four_b_full_window_peak_proximity":0.819,"four_b_timing_verdict":"price_only_local_4B_watch_not_full_4B","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"hard_4c_success_after_no_conversion","trigger_outcome_label":"false_positive_high_mfe_high_mae_roundtrip","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; historical corporate candidates exist outside window","same_entry_group_id":"R4L74_C15_025820_20240404_COPPER_PROXY_PRICE_ONLY_SPIKE::2024-04-04","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R4L74_C15_012800_STAGE2_FP_20240404","case_id":"R4L74_C15_012800_20240404_COPPER_PROXY_SMALLCAP_SPIKE","symbol":"012800","company_name":"대창","round":"R4","loop":"74","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","fine_archetype_id":"COPPER_SPREAD_PRODUCER_CONVERSION_VS_PRICE_PROXY","sector":"materials_nonferrous_copper","primary_archetype":"material_spread_supercycle","loop_objective":"sector_specific_rule_discovery|counterexample_mining|4B_non_price_requirement_stress_test","trigger_type":"Stage2-FalsePositive","trigger_date":"2024-04-04","evidence_available_at_that_date":"Copper beta and small-cap thematic flow were visible, but no durable margin bridge, no customer-quality evidence, and no confirmed revision path were available at trigger date.","evidence_source":"historical public-event proxy: copper thematic rally + stock-web price rows; company-specific margin evidence not used","stage2_evidence_fields":["relative_strength","policy_or_regulatory_optionality"],"stage3_evidence_fields":[],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/012/012800/2024.csv","profile_path":"atlas/symbol_profiles/012/012800.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-04","entry_price":1470,"MFE_30D_pct":57.82,"MFE_90D_pct":57.82,"MFE_180D_pct":57.82,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-4.76,"MAE_90D_pct":-25.17,"MAE_180D_pct":-25.17,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-21","peak_price":2320,"drawdown_after_peak_pct":-52.59,"green_lateness_ratio":"not_applicable:no_confirmed_Stage3_Green_trigger","four_b_local_peak_proximity":0.829,"four_b_full_window_peak_proximity":0.829,"four_b_timing_verdict":"price_only_local_4B_watch_not_full_4B","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"hard_4c_success_after_theme_fade","trigger_outcome_label":"false_positive_price_proxy_roundtrip","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window; historical corporate candidates exist outside window","same_entry_group_id":"R4L74_C15_012800_20240404_COPPER_PROXY_SMALLCAP_SPIKE::2024-04-04","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L74_C15_103140_20240222_COPPER_DEFENSE_MARGIN_BRIDGE","trigger_id":"R4L74_C15_103140_STAGE2A_20240222","symbol":"103140","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":5,"backlog_visibility_score":6,"margin_bridge_score":6,"revision_score":4,"relative_strength_score":7,"customer_quality_score":4,"policy_or_regulatory_score":3,"valuation_repricing_score":2,"execution_risk_score":-1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":6,"producer_conversion_score":6},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":5,"backlog_visibility_score":6,"margin_bridge_score":8,"revision_score":5,"relative_strength_score":7,"customer_quality_score":4,"policy_or_regulatory_score":3,"valuation_repricing_score":2,"execution_risk_score":-1,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":7,"producer_conversion_score":8},"weighted_score_after":82,"stage_label_after":"Stage3-Yellow / Stage2-Actionable-confirmed","changed_components":["margin_bridge_score","relative_strength_score","execution_risk_score","asp_or_spread_score","producer_conversion_score"],"component_delta_explanation":"C15 copper spread proxy is promoted only when commodity tailwind converts into producer-level margin/revision/order evidence; pure price beta is capped as Stage2-Watch and routed to 4B/4C guard after local peak.","MFE_90D_pct":86.97,"MAE_90D_pct":-7.7,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L74_C15_025820_20240404_COPPER_PROXY_PRICE_ONLY_SPIKE","trigger_id":"R4L74_C15_025820_STAGE2_FP_20240404","symbol":"025820","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":5,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":4,"producer_conversion_score":0},"weighted_score_before":76,"stage_label_before":"Stage3-Yellow / false Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":6,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":3,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":2,"producer_conversion_score":0},"weighted_score_after":64,"stage_label_after":"Stage2-Watch / blocked_positive_stage","changed_components":["margin_bridge_score","relative_strength_score","execution_risk_score","asp_or_spread_score","producer_conversion_score"],"component_delta_explanation":"C15 copper spread proxy is promoted only when commodity tailwind converts into producer-level margin/revision/order evidence; pure price beta is capped as Stage2-Watch and routed to 4B/4C guard after local peak.","MFE_90D_pct":55.06,"MAE_90D_pct":-30.11,"score_return_alignment_label":"current_false_positive_corrected_by_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R4L74_C15_012800_20240404_COPPER_PROXY_SMALLCAP_SPIKE","trigger_id":"R4L74_C15_012800_STAGE2_FP_20240404","symbol":"012800","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":1,"revision_score":0,"relative_strength_score":8,"customer_quality_score":0,"policy_or_regulatory_score":4,"valuation_repricing_score":5,"execution_risk_score":-2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":4,"producer_conversion_score":0},"weighted_score_before":75,"stage_label_before":"Stage3-Yellow / false Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":0,"relative_strength_score":6,"customer_quality_score":0,"policy_or_regulatory_score":2,"valuation_repricing_score":3,"execution_risk_score":-5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"asp_or_spread_score":2,"producer_conversion_score":0},"weighted_score_after":62,"stage_label_after":"Stage2-Watch / blocked_positive_stage","changed_components":["margin_bridge_score","relative_strength_score","execution_risk_score","asp_or_spread_score","producer_conversion_score"],"component_delta_explanation":"C15 copper spread proxy is promoted only when commodity tailwind converts into producer-level margin/revision/order evidence; pure price beta is capped as Stage2-Watch and routed to 4B/4C guard after local peak.","MFE_90D_pct":57.82,"MAE_90D_pct":-25.17,"score_return_alignment_label":"current_false_positive_corrected_by_guard","current_profile_verdict":"current_profile_false_positive"}
```

### 25.5 score profile comparison rows

```jsonl
{"row_type":"aggregate_profile_comparison","profile_id":"P0_e2r_2_1_stock_web_calibrated_proxy","profile_scope":"current_proxy","profile_hypothesis":"Current global calibration catches price-only blowoff in general but can still over-promote commodity price beta if spread evidence is treated as company evidence.","changed_axes":[],"changed_thresholds":{},"eligible_trigger_count":3,"selected_entry_trigger_per_case":"representative","avg_MFE_90D_pct":66.62,"avg_MAE_90D_pct":-20.99,"avg_MFE_180D_pct":66.62,"avg_MAE_180D_pct":-20.99,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":1,"avg_green_lateness_ratio":"0.32 among cases with Green trigger","avg_four_b_local_peak_proximity":0.821,"avg_four_b_full_window_peak_proximity":0.821,"score_return_alignment_verdict":"mixed; positive recognized but two copper proxies need company-conversion guard"}
{"row_type":"aggregate_profile_comparison","profile_id":"P0b_e2r_2_0_baseline_reference","profile_scope":"rollback_reference","profile_hypothesis":"Older baseline would accept relative strength and commodity theme too easily.","changed_axes":["none; reference only"],"changed_thresholds":{},"eligible_trigger_count":3,"selected_entry_trigger_per_case":"representative","avg_MFE_90D_pct":66.62,"avg_MAE_90D_pct":-20.99,"avg_MFE_180D_pct":66.62,"avg_MAE_180D_pct":-20.99,"false_positive_rate":0.67,"missed_structural_count":0,"late_green_count":1,"avg_green_lateness_ratio":"0.32 among cases with Green trigger","avg_four_b_local_peak_proximity":0.821,"avg_four_b_full_window_peak_proximity":0.821,"score_return_alignment_verdict":"weaker than P0; price proxy false positives pass too often"}
{"row_type":"aggregate_profile_comparison","profile_id":"P1_sector_specific_candidate_profile","profile_scope":"sector_specific","profile_hypothesis":"Within L4, commodity price evidence must be separated from company-level producer conversion evidence.","changed_axes":["producer_conversion_min_evidence_family_count>=2","price_proxy_positive_stage_cap=Stage2-Watch"],"changed_thresholds":{"producer_conversion_min_evidence_family_count":2,"proxy_only_stage_cap":"Stage2-Watch"},"eligible_trigger_count":3,"selected_entry_trigger_per_case":"representative","avg_MFE_90D_pct":86.97,"avg_MAE_90D_pct":-7.7,"avg_MFE_180D_pct":86.97,"avg_MAE_180D_pct":-7.7,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":0.32,"avg_four_b_local_peak_proximity":0.815,"avg_four_b_full_window_peak_proximity":0.815,"score_return_alignment_verdict":"best precision; keeps producer success and blocks price-beta proxies"}
{"row_type":"aggregate_profile_comparison","profile_id":"P2_canonical_archetype_candidate_profile","profile_scope":"canonical_archetype_specific","profile_hypothesis":"For C15, spread supercycle score needs realized ASP/margin/revision bridge, not only commodity screen or RS.","changed_axes":["c15_spread_to_earnings_bridge_bonus=+3","c15_proxy_without_conversion_penalty=-8"],"changed_thresholds":{"stage2_actionable_company_conversion_min":2},"eligible_trigger_count":3,"selected_entry_trigger_per_case":"representative","avg_MFE_90D_pct":86.97,"avg_MAE_90D_pct":-7.7,"avg_MFE_180D_pct":86.97,"avg_MAE_180D_pct":-7.7,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":0.32,"avg_four_b_local_peak_proximity":0.815,"avg_four_b_full_window_peak_proximity":0.815,"score_return_alignment_verdict":"canonical rule candidate; more precise than global price-only guard"}
{"row_type":"aggregate_profile_comparison","profile_id":"P3_counterexample_guard_profile","profile_scope":"counterexample_guard","profile_hypothesis":"If copper proxy lacks producer conversion, Stage2 promotion is blocked and local peak becomes watch-only 4B overlay.","changed_axes":["price_proxy_local_peak_guard","hard_4c_after_theme_fade_without_margin_bridge"],"changed_thresholds":{"min_margin_bridge_score_for_green":5},"eligible_trigger_count":2,"selected_entry_trigger_per_case":"025820|012800","avg_MFE_90D_pct":56.44,"avg_MAE_90D_pct":-27.64,"avg_MFE_180D_pct":56.44,"avg_MAE_180D_pct":-27.64,"false_positive_rate":0.0,"missed_structural_count":0,"late_green_count":0,"avg_green_lateness_ratio":"not_applicable","avg_four_b_local_peak_proximity":0.824,"avg_four_b_full_window_peak_proximity":0.824,"score_return_alignment_verdict":"counterexample guard improves MAE and false-positive rate"}
```

### 25.6 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c15_price_proxy_positive_stage_cap,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,none,Stage2-Watch,cap,"Copper price beta without company conversion produced high MFE but high MAE and roundtrip risk","false_positive_rate 0.67 -> 0.00 in sample; avg MAE selected cases improves by excluding proxy false positives","R4L74_C15_025820_STAGE2_FP_20240404|R4L74_C15_012800_STAGE2_FP_20240404",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c15_producer_conversion_bridge_bonus,canonical_archetype_specific,L4_MATERIALS_SPREAD_RESOURCE,C15_MATERIAL_SPREAD_SUPERCYCLE,0,+3,+3,"Producer-level margin/revision/order evidence separated 풍산 from copper-beta proxies","retains structural success 103140 while blocking two false positives","R4L74_C15_103140_STAGE2A_20240222",3,3,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
```

### 25.7 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R4","loop":"74","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","scheduled_round":"R4","scheduled_loop":74,"round_schedule_status":"valid","round_sector_consistency":"pass","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_trigger_family_count":3,"positive_case_count":1,"counterexample_count":2,"current_profile_error_count":2,"diversity_score_summary":"new_symbols=3;new_trigger_families=3;counterexample_gap=2;wrong_round_penalty=0;schema_rematerialization_penalty=0","tested_existing_calibrated_axes":["price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["commodity_price_proxy_false_positive","local_peak_watch_should_not_be_full_4B"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
```

### 25.8 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"none","symbol":"none","large_sector_id":"L4_MATERIALS_SPREAD_RESOURCE","canonical_archetype_id":"C15_MATERIAL_SPREAD_SUPERCYCLE","reason":"all selected cases had sufficient 180D stock-web windows","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_loop = 74
next_round = R5
next_loop = 74
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Stock-Web manifest checked: `atlas/manifest.json`; manifest max_date = 2026-02-20; tradable_row_count = 14,354,401.
- Stock-Web schema checked: `atlas/schema.json`; MFE/MAE formula and calibration usable rules follow schema fields.
- Symbol profiles checked: `103140`, `025820`, `012800`; all selected 2024 180D windows are clean against corporate-action dates.
- Price shards checked: `atlas/ohlcv_tradable_by_symbol_year/103/103140/2024.csv`, `atlas/ohlcv_tradable_by_symbol_year/025/025820/2024.csv`, `atlas/ohlcv_tradable_by_symbol_year/012/012800/2024.csv`.
- Research artifact used for duplicate avoidance only: `docs/core/V12_Research_No_Repeat_Index.md`; `stock_agent/src` was not opened.
