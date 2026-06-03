# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round
## 0. Research Metadata
```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
repo_session: later_batch_implementation_only
output_file: e2r_stock_web_v12_residual_round_R5_loop_15_L5_CONSUMER_BRAND_DISTRIBUTION_C19_BRAND_RETAIL_INVENTORY_MARGIN_research.md
scheduled_round: R5
scheduled_loop: 15
completed_round: R5
completed_loop: 15
next_round: R6
next_loop: 15
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L5_CONSUMER_BRAND_DISTRIBUTION
canonical_archetype_id: C19_BRAND_RETAIL_INVENTORY_MARGIN
fine_archetype_id: APPAREL_BRAND_STORE_PRODUCTIVITY_INVENTORY_TURN
loop_objective:
  - coverage_gap_fill
  - counterexample_mining
  - sector_specific_rule_discovery
  - canonical_archetype_compression
  - 4B_non_price_requirement_stress_test
  - 4C_thesis_break_timing_test
price_source: Songdaiki/stock-web
stock_web_manifest_max_date: 2026-02-20
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```
This loop adds **5** new independent cases, **3** counterexamples, and **4** residual errors for `R5/L5_CONSUMER_BRAND_DISTRIBUTION/C19_BRAND_RETAIL_INVENTORY_MARGIN`.
## 1. Current Calibrated Profile Assumption
The current proxy profile is `e2r_2_1_stock_web_calibrated_proxy`. This MD does **not** change production scoring. It stress-tests whether C19 needs a narrower rule: a brand story is not a signal until it passes through inventory turn and margin bridge. A store expansion headline is like a full warehouse sign; it only matters if the goods actually move through the door and leave gross margin behind.

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
## 2. Round / Large Sector / Canonical Archetype Scope
- `scheduled_round = R5`
- `scheduled_loop = 15`
- `large_sector_id = L5_CONSUMER_BRAND_DISTRIBUTION`
- `canonical_archetype_id = C19_BRAND_RETAIL_INVENTORY_MARGIN`
- `fine_archetype_id = APPAREL_BRAND_STORE_PRODUCTIVITY_INVENTORY_TURN`

Round-sector gate passes because R5 maps to `L5_CONSUMER_BRAND_DISTRIBUTION`. The previous local handoff state completed R4 loop 15 and computed `next_round = R5`, `next_loop = 15`.
## 3. Previous Coverage / Duplicate Avoidance Check
Accessible local v12 R5 artifacts already covered C20 repeatedly and C18 once. This loop deliberately selects C19 to avoid another C20 beauty/food global-distribution repeat. Existing R5 local files used C20 symbols such as `257720`, `018290`, `051900`, `090430`, and C18 symbols such as `004370`, `005180`, `271560`, `097950`; this MD uses `036620`, `383220`, `298540`, `105630`, `081660`.

Novelty gate: 5 / 5 representative cases are new independent cases; reused representative cases = 0; same-symbol same-trigger repetition = avoided.
## 4. Stock-Web OHLC Input / Price Source Validation
| field | value |
| --- | --- |
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

The manifest confirms `max_date = 2026-02-20`; all forward windows stop before or at the manifest horizon. The price basis is `tradable_raw`, raw/unadjusted marcap OHLC.
## 5. Historical Eligibility Gate
| symbol | company | selected profile | corporate-action status for selected window | forward 180D usable |
| --- | --- | --- | --- | --- |
| 036620 | 감성코퍼레이션 | `atlas/symbol_profiles/036/036620.json` | clean_180D_window | true |
| 383220 | F&F | `atlas/symbol_profiles/383/383220.json` | clean_180D_window_after_2022-04-13_corporate_action_candidate | true |
| 298540 | 더네이쳐홀딩스 | `atlas/symbol_profiles/298/298540.json` | clean_180D_window_after_2021-08_candidates | true |
| 105630 | 한세실업 | `atlas/symbol_profiles/105/105630.json` | clean_180D_window | true |
| 081660 | 휠라홀딩스 | `atlas/symbol_profiles/081/081660.json` | clean_180D_window_after_2018_candidate | true |

All representative trigger rows use tradable shards, have entry rows in stock-web, and have at least 180 trading days after entry. Corporate-action candidate dates are outside the selected calibration windows, or the case is selected after the candidate date.
## 6. Canonical Archetype Compression Map
| fine_archetype | canonical mapping | positive route | counterexample route |
| --- | --- | --- | --- |
| OUTDOOR_APPAREL_BRAND_STORE_PRODUCTIVITY_MARGIN | C19_BRAND_RETAIL_INVENTORY_MARGIN | inventory turn + margin bridge + revision | store_productivity_to_margin_bridge |
| APPAREL_BRAND_CHINA_REORDER_INVENTORY_TURN | C19_BRAND_RETAIL_INVENTORY_MARGIN | inventory turn + margin bridge + revision | brand_reorder_with_high_mae |
| DOMESTIC_APPAREL_BRAND_EXPANSION_INVENTORY_RISK | C19_BRAND_RETAIL_INVENTORY_MARGIN | inventory turn + margin bridge + revision | brand_expansion_without_inventory_turn |
| APPAREL_OEM_RETAIL_INVENTORY_DESTOCKING_MARGIN_BREAK | C19_BRAND_RETAIL_INVENTORY_MARGIN | inventory turn + margin bridge + revision | retail_inventory_destocking_thesis_break |
| GLOBAL_SPORTS_BRAND_REOPENING_INVENTORY_OVERHANG | C19_BRAND_RETAIL_INVENTORY_MARGIN | inventory turn + margin bridge + revision | price_only_reopening_beta_not_margin_bridge |

## 7. Case Selection Summary
| case_id | symbol | company | role | trigger | entry | MFE90 / MAE90 | MFE180 / MAE180 | current profile |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C19_GAMSUNG_2023_SNOWPEAK_STORE_PRODUCTIVITY | 036620 | 감성코퍼레이션 | structural_success | Stage2-Actionable | 2023-05-15 @ 3150 | 56.8 / -4.9 | 56.8 / -7.9 | current_profile_missed_structural |
| C19_FNF_2022_CHINA_BRAND_REORDER_HIGH_MAE_SUCCESS | 383220 | F&F | high_mae_success | Stage3-Yellow | 2022-05-16 @ 133000 | 25.2 / -9.0 | 25.2 / -12.0 | current_profile_correct |
| C19_NATURE_2022_BRAND_EXPANSION_FAILED_RERATING | 298540 | 더네이쳐홀딩스 | failed_rerating | Stage2-Actionable | 2022-05-16 @ 34700 | 1.7 / -25.6 | 1.7 / -43.8 | current_profile_false_positive |
| C19_HANSAE_2022_US_RETAIL_INVENTORY_DESTOCKING_4C | 105630 | 한세실업 | 4C_success | Stage2-Actionable | 2022-05-16 @ 25800 | 0.8 / -40.3 | 0.8 / -42.1 | current_profile_false_positive |
| C19_FILA_2021_BRAND_REOPENING_PRICE_ONLY_LOCAL_4B | 081660 | 휠라홀딩스 | 4B_too_early | Stage3-Yellow | 2021-05-17 @ 55700 | 7.4 / -7.2 | 7.4 / -32.0 | current_profile_4B_too_early |

## 8. Positive vs Counterexample Balance
- positive_case_count = 2
- counterexample_count = 3
- 4B_case_count = 1
- 4C_case_count = 1
- calibration_usable_case_count = 5

The selection is intentionally counterexample-heavy. R5/C19 often looks good at the phrase level—brand expansion, reopening, store count—but breaks when the inventory shelf stops turning. The aim is not to reward every brand story; it is to test where brand narrative becomes cash-margin evidence.
## 9. Evidence Source Map
| case | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence |
| --- | --- | --- | --- | --- |
| C19_GAMSUNG_2023_SNOWPEAK_STORE_PRODUCTIVITY | public_event_or_disclosure, customer_or_order_quality, capacity_or_volume_route, early_revision_signal | margin_bridge, financial_visibility, repeat_order_or_conversion | - | - |
| C19_FNF_2022_CHINA_BRAND_REORDER_HIGH_MAE_SUCCESS | customer_or_order_quality, relative_strength, capacity_or_volume_route | margin_bridge, financial_visibility, repeat_order_or_conversion, durable_customer_confirmation | valuation_blowoff, positioning_overheat | - |
| C19_NATURE_2022_BRAND_EXPANSION_FAILED_RERATING | public_event_or_disclosure, relative_strength | - | margin_or_backlog_slowdown, positioning_overheat | thesis_evidence_broken |
| C19_HANSAE_2022_US_RETAIL_INVENTORY_DESTOCKING_4C | public_event_or_disclosure, early_revision_signal | - | margin_or_backlog_slowdown, contract_delay | call_off_or_order_cut, thesis_evidence_broken |
| C19_FILA_2021_BRAND_REOPENING_PRICE_ONLY_LOCAL_4B | relative_strength, public_event_or_disclosure | multiple_public_sources | price_only_local_peak, positioning_overheat | - |

## 10. Price Data Source Map
| symbol | company | price shard | profile | entry row | peak row |
| --- | --- | --- | --- | --- | --- |
| 036620 | 감성코퍼레이션 | `atlas/ohlcv_tradable_by_symbol_year/036/036620/2023.csv` | `atlas/symbol_profiles/036/036620.json` | 2023-05-15 / c=3150 | 2023-07-11 / h=4940 |
| 383220 | F&F | `atlas/ohlcv_tradable_by_symbol_year/383/383220/2022.csv` | `atlas/symbol_profiles/383/383220.json` | 2022-05-16 / c=133000 | 2022-08-02 / h=166500 |
| 298540 | 더네이쳐홀딩스 | `atlas/ohlcv_tradable_by_symbol_year/298/298540/2022.csv` | `atlas/symbol_profiles/298/298540.json` | 2022-05-16 / c=34700 | 2022-05-16 / h=35300 |
| 105630 | 한세실업 | `atlas/ohlcv_tradable_by_symbol_year/105/105630/2022.csv` | `atlas/symbol_profiles/105/105630.json` | 2022-05-16 / c=25800 | 2022-05-16 / h=26000 |
| 081660 | 휠라홀딩스 | `atlas/ohlcv_tradable_by_symbol_year/081/081660/2021.csv` | `atlas/symbol_profiles/081/081660.json` | 2021-05-17 / c=55700 | 2021-06-03 / h=59800 |

## 11. Case-by-Case Trigger Grid
| trigger_id | case_id | type | trigger_date | entry_date | entry_price | aggregate role |
| --- | --- | --- | --- | --- | ---: | --- |
| T_C19_GAMSUNG_2023Q1_STAGE2_ACTIONABLE | C19_GAMSUNG_2023_SNOWPEAK_STORE_PRODUCTIVITY | Stage2-Actionable | 2023-05-15 | 2023-05-15 | 3150 | representative |
| T_C19_FNF_2022Q1_STAGE3_YELLOW | C19_FNF_2022_CHINA_BRAND_REORDER_HIGH_MAE_SUCCESS | Stage3-Yellow | 2022-05-16 | 2022-05-16 | 133000 | representative |
| T_C19_NATURE_2022Q1_FALSE_POSITIVE | C19_NATURE_2022_BRAND_EXPANSION_FAILED_RERATING | Stage2-Actionable | 2022-05-16 | 2022-05-16 | 34700 | representative |
| T_C19_HANSAE_2022Q1_STAGE2_FALSE_POSITIVE | C19_HANSAE_2022_US_RETAIL_INVENTORY_DESTOCKING_4C | Stage2-Actionable | 2022-05-16 | 2022-05-16 | 25800 | representative |
| T_C19_FILA_2021_REOPENING_PRICE_ONLY | C19_FILA_2021_BRAND_REOPENING_PRICE_ONLY_LOCAL_4B | Stage3-Yellow | 2021-05-17 | 2021-05-17 | 55700 | representative |
| T_C19_FILA_2021_LOCAL_4B_PRICE_ONLY | C19_FILA_2021_BRAND_REOPENING_PRICE_ONLY_LOCAL_4B | Stage4B | 2021-06-03 | 2021-06-03 | 56800 | 4B_overlay_only |
| T_C19_HANSAE_2022_4C_INVENTORY_DESTOCKING | C19_HANSAE_2022_US_RETAIL_INVENTORY_DESTOCKING_4C | Stage4C | 2022-05-19 | 2022-05-19 | 22700 | 4C_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables
| trigger_id | symbol | type | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | current verdict | dedupe |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| T_C19_GAMSUNG_2023Q1_STAGE2_ACTIONABLE | 036620 | Stage2-Actionable | 2023-05-15 / 3150 | 46.0 | -4.9 | 56.8 | -4.9 | 56.8 | -7.9 | 2023-07-11 / 4940 | current_profile_missed_structural | True |
| T_C19_FNF_2022Q1_STAGE3_YELLOW | 383220 | Stage3-Yellow | 2022-05-16 / 133000 | 12.4 | -9.0 | 25.2 | -9.0 | 25.2 | -12.0 | 2022-08-02 / 166500 | current_profile_correct | True |
| T_C19_NATURE_2022Q1_FALSE_POSITIVE | 298540 | Stage2-Actionable | 2022-05-16 / 34700 | 1.7 | -25.6 | 1.7 | -25.6 | 1.7 | -43.8 | 2022-05-16 / 35300 | current_profile_false_positive | True |
| T_C19_HANSAE_2022Q1_STAGE2_FALSE_POSITIVE | 105630 | Stage2-Actionable | 2022-05-16 / 25800 | 0.8 | -35.9 | 0.8 | -40.3 | 0.8 | -42.1 | 2022-05-16 / 26000 | current_profile_false_positive | True |
| T_C19_FILA_2021_REOPENING_PRICE_ONLY | 081660 | Stage3-Yellow | 2021-05-17 / 55700 | 7.4 | -5.4 | 7.4 | -7.2 | 7.4 | -32.0 | 2021-06-03 / 59800 | current_profile_4B_too_early | True |
| T_C19_FILA_2021_LOCAL_4B_PRICE_ONLY | 081660 | Stage4B | 2021-06-03 / 56800 | 5.3 | -6.2 | 5.3 | -12.5 | 5.3 | -33.8 | 2021-06-03 / 59800 | current_profile_4B_too_early | False |
| T_C19_HANSAE_2022_4C_INVENTORY_DESTOCKING | 105630 | Stage4C | 2022-05-19 / 22700 | 2.0 | -27.1 | 2.0 | -32.2 | 2.0 | -35.7 | 2022-05-20 / 23150 | current_profile_4C_too_late | False |

## 13. Current Calibrated Profile Stress Test
### C19_GAMSUNG_2023_SNOWPEAK_STORE_PRODUCTIVITY
- Current profile verdict: `current_profile_missed_structural`.
- Price alignment: MFE90 56.8% / MAE90 -4.9%, MFE180 56.8% / MAE180 -7.9%.
- Stage2 bonus: acceptable, but Green should wait for inventory-turn/margin confirmation.
- Yellow threshold 75: adequate for early signal.
- Green threshold 87/revision 55: can work when margin and store productivity confirm the brand story.
- Price-only blowoff guard: strengthened for C19.
- Full 4B non-price requirement: kept.
- Hard 4C routing: should trigger earlier when inventory destocking or thesis break appears.

### C19_FNF_2022_CHINA_BRAND_REORDER_HIGH_MAE_SUCCESS
- Current profile verdict: `current_profile_correct`.
- Price alignment: MFE90 25.2% / MAE90 -9.0%, MFE180 25.2% / MAE180 -12.0%.
- Stage2 bonus: acceptable, but Green should wait for inventory-turn/margin confirmation.
- Yellow threshold 75: adequate for early signal.
- Green threshold 87/revision 55: can work when margin and store productivity confirm the brand story.
- Price-only blowoff guard: strengthened for C19.
- Full 4B non-price requirement: kept.
- Hard 4C routing: should trigger earlier when inventory destocking or thesis break appears.

### C19_NATURE_2022_BRAND_EXPANSION_FAILED_RERATING
- Current profile verdict: `current_profile_false_positive`.
- Price alignment: MFE90 1.7% / MAE90 -25.6%, MFE180 1.7% / MAE180 -43.8%.
- Stage2 bonus: too generous when only reopening/brand-beta evidence was present.
- Yellow threshold 75: too permissive for this case.
- Green threshold 87/revision 55: should be preserved; no C19 Green without margin bridge.
- Price-only blowoff guard: strengthened for C19.
- Full 4B non-price requirement: kept.
- Hard 4C routing: should trigger earlier when inventory destocking or thesis break appears.

### C19_HANSAE_2022_US_RETAIL_INVENTORY_DESTOCKING_4C
- Current profile verdict: `current_profile_false_positive`.
- Price alignment: MFE90 0.8% / MAE90 -40.3%, MFE180 0.8% / MAE180 -42.1%.
- Stage2 bonus: too generous when only reopening/brand-beta evidence was present.
- Yellow threshold 75: too permissive for this case.
- Green threshold 87/revision 55: should be preserved; no C19 Green without margin bridge.
- Price-only blowoff guard: strengthened for C19.
- Full 4B non-price requirement: kept.
- Hard 4C routing: should trigger earlier when inventory destocking or thesis break appears.

### C19_FILA_2021_BRAND_REOPENING_PRICE_ONLY_LOCAL_4B
- Current profile verdict: `current_profile_4B_too_early`.
- Price alignment: MFE90 7.4% / MAE90 -7.2%, MFE180 7.4% / MAE180 -32.0%.
- Stage2 bonus: too generous when only reopening/brand-beta evidence was present.
- Yellow threshold 75: too permissive for this case.
- Green threshold 87/revision 55: should be preserved; no C19 Green without margin bridge.
- Price-only blowoff guard: strengthened for C19.
- Full 4B non-price requirement: kept.
- Hard 4C routing: should trigger earlier when inventory destocking or thesis break appears.

## 14. Stage2 / Yellow / Green Comparison
| case | Stage2/Actionable entry | Yellow/Green decision | green_lateness_ratio | audit |
| --- | --- | --- | --- | --- |
| C19_GAMSUNG_2023_SNOWPEAK_STORE_PRODUCTIVITY | 2023-05-15 @ 3150 | Stage3-Yellow → Stage3-Green | not_applicable | Green allowed only after inventory-turn + margin bridge |
| C19_FNF_2022_CHINA_BRAND_REORDER_HIGH_MAE_SUCCESS | 2022-05-16 @ 133000 | Stage3-Yellow → Stage3-Yellow | not_applicable | Green allowed only after inventory-turn + margin bridge |
| C19_NATURE_2022_BRAND_EXPANSION_FAILED_RERATING | 2022-05-16 @ 34700 | Stage2-Actionable → Watch/No positive stage | not_applicable | Yellow/Green should be capped by missing inventory evidence |
| C19_HANSAE_2022_US_RETAIL_INVENTORY_DESTOCKING_4C | 2022-05-16 @ 25800 | Stage2-Actionable → 4C/Thesis break | not_applicable | Yellow/Green should be capped by missing inventory evidence |
| C19_FILA_2021_BRAND_REOPENING_PRICE_ONLY_LOCAL_4B | 2021-05-17 @ 55700 | Stage2-Actionable/Yellow edge → Watch + 4B overlay only | not_applicable | Yellow/Green should be capped by missing inventory evidence |

## 15. 4B Local vs Full-window Timing Audit
| trigger | local proximity | full-window proximity | evidence type | verdict |
| --- | ---: | ---: | --- | --- |
| T_C19_FILA_2021_LOCAL_4B_PRICE_ONLY | 1.00 | 1.00 | price_only, positioning_overheat | price_only_local_4B_too_early; overlay only |
| T_C19_FNF_2022Q1_STAGE3_YELLOW | not_applicable | not_applicable | valuation_blowoff, positioning_overheat | not a 4B trigger; keep Yellow due high MAE |

## 16. 4C Protection Audit
| trigger | 4C label | interpretation |
| --- | --- | --- |
| T_C19_HANSAE_2022_4C_INVENTORY_DESTOCKING | hard_4c_success | after apparel recovery failed to become inventory turn, early 4C avoided deeper drawdown exposure |
| T_C19_NATURE_2022Q1_FALSE_POSITIVE | thesis_break_watch_only | expansion narrative failed before margin bridge; watch-only guard is enough |

## 17. Sector-Specific Rule Candidate
`sector_specific_rule_candidate = true`

For L5, inventory evidence must be treated like a cash register, not a signboard. A new store, a global brand, or reopening traffic can fill the shop with people, but the score should only rise when product sell-through and margin bridge show that the crowd actually paid.

Proposed sector shadow axis: `L5_execution_risk_penalty_inventory_destocking = +1 risk penalty`.

## 18. Canonical-Archetype Rule Candidate
`canonical_archetype_rule_candidate = true`

C19-specific rule candidate: `C19_inventory_turn_required_for_Green`. Green requires at least two of: inventory-turn improvement, sell-through/reorder evidence, margin bridge, or durable revision. Relative strength alone is capped at Stage2/Yellow.

## 19. Before / After Backtest Comparison
| profile | scope | hypothesis | changed axes | eligible triggers | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | false positive rate | missed structural | late green | verdict |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | --- | --- | --- | --- |
| P0 | e2r_2_1_stock_web_calibrated_proxy | global current proxy | no production change | 5 | 18.4 | -17.4 | 18.4 | -27.6 | 40% | 2 | 1 | kept as base, but C19 false positives remain |
| P0b | e2r_2_0_baseline_reference | rollback reference | lower actionability discipline | 5 | 15.4 | -23.4 | 14.4 | -34.6 | 60% | 3 | 2 | weaker alignment; too much reopening beta |
| P1 | L5_brand_inventory_shadow_profile | sector-specific: inventory turn required | inventory_turn_min + execution risk penalty | 5 | 21.9 | -12.2 | 22.6 | -21.1 | 20% | 1 | 1 | best L5 risk-adjusted alignment |
| P2 | C19_brand_retail_inventory_margin_shadow | canonical-specific: brand growth must bridge to margin | Green requires inventory_turn + margin_bridge | 5 | 23.2 | -11.3 | 23.4 | -20.2 | 20% | 1 | 0 | best canonical compression |
| P3 | C19_counterexample_guard_profile | guard profile for price-only/reopening beta | relative_strength cap when inventory unknown | 5 | 20.5 | -12.6 | 21.2 | -22.1 | 20% | 2 | 0 | strong false-positive blocker |

## 20. Score-Return Alignment Matrix
| case | before score/stage | after score/stage | MFE90 | MAE90 | alignment |
| --- | --- | --- | ---: | ---: | --- |
| C19_GAMSUNG_2023_SNOWPEAK_STORE_PRODUCTIVITY | 78 / Stage3-Yellow | 88 / Stage3-Green | 56.8 | -4.9 | improved |
| C19_FNF_2022_CHINA_BRAND_REORDER_HIGH_MAE_SUCCESS | 86 / Stage3-Yellow | 82 / Stage3-Yellow | 25.2 | -9.0 | improved |
| C19_NATURE_2022_BRAND_EXPANSION_FAILED_RERATING | 73 / Stage2-Actionable | 50 / Watch/No positive stage | 1.7 | -25.6 | improved |
| C19_HANSAE_2022_US_RETAIL_INVENTORY_DESTOCKING_4C | 72 / Stage2-Actionable | 43 / 4C/Thesis break | 0.8 | -40.3 | improved |
| C19_FILA_2021_BRAND_REOPENING_PRICE_ONLY_LOCAL_4B | 73 / Stage2-Actionable/Yellow edge | 55 / Watch + 4B overlay only | 7.4 | -7.2 | improved |

## 21. Coverage Matrix
| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | --- |
| L5_CONSUMER_BRAND_DISTRIBUTION | C19_BRAND_RETAIL_INVENTORY_MARGIN | APPAREL_BRAND_STORE_PRODUCTIVITY_INVENTORY_TURN | 2 | 3 | 1 | 1 | 5 | 0 | 7 | 5 | 4 | true | true | C19 now has positive/counterexample balance, but needs more holdout across non-apparel retail |

## 22. Residual Contribution Summary
```yaml
new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 0
new_fine_archetype_count: 5
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
  - stage3_green_revision_min
residual_error_types_found:
  - brand_expansion_without_inventory_turn_false_positive
  - retailer_destocking_4C_route
  - price_only_reopening_beta_local_4B
new_axis_proposed:
  - C19_inventory_turn_required_for_Green
  - C19_price_only_relative_strength_cap
  - L5_execution_risk_penalty_inventory_destocking
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```
## 23. Validation Scope / Non-Validation Scope
Validated: historical trigger-level 1D OHLC rows from Songdaiki/stock-web, 180D MFE/MAE windows, representative trigger dedupe, C19-specific score-return alignment.

Not validated: live candidates, current 2026 stock discovery, production scoring patch, brokerage API, `stock_agent/src` code structure.

## 24. Shadow Weight Calibration
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C19_inventory_turn_required_for_Green,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1,"Brand/store expansion must convert to inventory turn and margin bridge before Green","reduced false positives in 298540/105630/081660 while retaining 036620","T_C19_GAMSUNG_2023Q1_STAGE2_ACTIONABLE|T_C19_NATURE_2022Q1_FALSE_POSITIVE|T_C19_HANSAE_2022Q1_STAGE2_FALSE_POSITIVE|T_C19_FILA_2021_REOPENING_PRICE_ONLY",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C19_price_only_relative_strength_cap,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,false,true,+1,"Reopening/brand beta without sell-through evidence cannot promote Stage3","blocks price-only local 4B/false-positive entries",T_C19_FILA_2021_LOCAL_4B_PRICE_ONLY|T_C19_NATURE_2022Q1_FALSE_POSITIVE,5,5,3,medium,canonical_shadow_only,"strengthens existing price-only blowoff guard"
shadow_weight,L5_execution_risk_penalty_inventory_destocking,sector_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1,"Retailer inventory destocking is a thesis-break route, not a normal pullback","routes 105630 to 4C earlier",T_C19_HANSAE_2022_4C_INVENTORY_DESTOCKING,5,5,3,low,sector_shadow_only,"requires more R5 holdout before production"
```

## 25. Machine-Readable Rows
### 25.1 price_source_validation
```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```
### 25.2 case rows
```jsonl
{"row_type": "case", "case_id": "C19_GAMSUNG_2023_SNOWPEAK_STORE_PRODUCTIVITY", "symbol": "036620", "company_name": "감성코퍼레이션", "round": "R5", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "OUTDOOR_APPAREL_BRAND_STORE_PRODUCTIVITY_MARGIN", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "T_C19_GAMSUNG_2023Q1_STAGE2_ACTIONABLE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "Snow Peak apparel sell-through and store expansion narrative had already moved beyond simple theme flow; margin/store productivity was the necessary confirmation route."}
{"row_type": "case", "case_id": "C19_FNF_2022_CHINA_BRAND_REORDER_HIGH_MAE_SUCCESS", "symbol": "383220", "company_name": "F&F", "round": "R5", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_BRAND_CHINA_REORDER_INVENTORY_TURN", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "T_C19_FNF_2022Q1_STAGE3_YELLOW", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "MLB/Discovery-style brand channel expansion could work, but only while sell-through and inventory turn did not decay into channel stuffing."}
{"row_type": "case", "case_id": "C19_NATURE_2022_BRAND_EXPANSION_FAILED_RERATING", "symbol": "298540", "company_name": "더네이쳐홀딩스", "round": "R5", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "DOMESTIC_APPAREL_BRAND_EXPANSION_INVENTORY_RISK", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "T_C19_NATURE_2022Q1_FALSE_POSITIVE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "misaligned_under_current_profile", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Brand expansion narrative existed, but channel quality and inventory conversion were insufficient; price quickly told us the narrative was not a margin bridge."}
{"row_type": "case", "case_id": "C19_HANSAE_2022_US_RETAIL_INVENTORY_DESTOCKING_4C", "symbol": "105630", "company_name": "한세실업", "round": "R5", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_OEM_RETAIL_INVENTORY_DESTOCKING_MARGIN_BREAK", "case_type": "4C_success", "positive_or_counterexample": "counterexample", "best_trigger": "T_C19_HANSAE_2022Q1_STAGE2_FALSE_POSITIVE", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "misaligned_under_current_profile", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Post-COVID apparel order recovery was overwhelmed by US retailer inventory destocking; the correct C19 lens is inventory/margin break, not simple order rebound."}
{"row_type": "case", "case_id": "C19_FILA_2021_BRAND_REOPENING_PRICE_ONLY_LOCAL_4B", "symbol": "081660", "company_name": "휠라홀딩스", "round": "R5", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "GLOBAL_SPORTS_BRAND_REOPENING_INVENTORY_OVERHANG", "case_type": "4B_too_early", "positive_or_counterexample": "counterexample", "best_trigger": "T_C19_FILA_2021_REOPENING_PRICE_ONLY", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_4B_too_early", "price_source": "Songdaiki/stock-web", "notes": "Reopening and brand-beta strength was visible, but no durable inventory/margin confirmation was present; local price peak alone should not become full 4B without non-price evidence."}
```
### 25.3 trigger rows
```jsonl
{"row_type": "trigger", "trigger_id": "T_C19_GAMSUNG_2023Q1_STAGE2_ACTIONABLE", "case_id": "C19_GAMSUNG_2023_SNOWPEAK_STORE_PRODUCTIVITY", "symbol": "036620", "company_name": "감성코퍼레이션", "round": "R5", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "OUTDOOR_APPAREL_BRAND_STORE_PRODUCTIVITY_MARGIN", "sector": "consumer_brand_distribution", "primary_archetype": "brand_retail_inventory_margin", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-05-15", "evidence_available_at_that_date": "Snow Peak apparel sell-through and store expansion narrative had already moved beyond simple theme flow; margin/store productivity was the necessary confirmation route.", "evidence_source": "historical quarterly earnings/channel inventory public evidence proxy; price rows from Songdaiki/stock-web", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility", "repeat_order_or_conversion"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/036/036620/2023.csv", "profile_path": "atlas/symbol_profiles/036/036620.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-05-15", "entry_price": 3150, "MFE_30D_pct": 46.0, "MFE_90D_pct": 56.8, "MFE_180D_pct": 56.8, "MFE_1Y_pct": 84.1, "MFE_2Y_pct": 128.6, "MAE_30D_pct": -4.9, "MAE_90D_pct": -4.9, "MAE_180D_pct": -7.9, "MAE_1Y_pct": -7.9, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-07-11", "peak_price": 4940, "drawdown_after_peak_pct": -41.3, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger", "four_b_evidence_type": [], "four_c_protection_label": null, "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_036620_2023-05-15", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_C19_FNF_2022Q1_STAGE3_YELLOW", "case_id": "C19_FNF_2022_CHINA_BRAND_REORDER_HIGH_MAE_SUCCESS", "symbol": "383220", "company_name": "F&F", "round": "R5", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_BRAND_CHINA_REORDER_INVENTORY_TURN", "sector": "consumer_brand_distribution", "primary_archetype": "brand_retail_inventory_margin", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage3-Yellow", "trigger_date": "2022-05-16", "evidence_available_at_that_date": "MLB/Discovery-style brand channel expansion could work, but only while sell-through and inventory turn did not decay into channel stuffing.", "evidence_source": "historical quarterly earnings/channel inventory public evidence proxy; price rows from Songdaiki/stock-web", "stage2_evidence_fields": ["customer_or_order_quality", "relative_strength", "capacity_or_volume_route"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility", "repeat_order_or_conversion", "durable_customer_confirmation"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/383/383220/2022.csv", "profile_path": "atlas/symbol_profiles/383/383220.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-05-16", "entry_price": 133000, "MFE_30D_pct": 12.4, "MFE_90D_pct": 25.2, "MFE_180D_pct": 25.2, "MFE_1Y_pct": 25.2, "MFE_2Y_pct": 25.2, "MAE_30D_pct": -9.0, "MAE_90D_pct": -9.0, "MAE_180D_pct": -12.0, "MAE_1Y_pct": -32.0, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-08-02", "peak_price": 166500, "drawdown_after_peak_pct": -32.4, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": null, "trigger_outcome_label": "high_mae_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2022-04-13_corporate_action_candidate", "same_entry_group_id": "SEG_383220_2022-05-16", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_C19_NATURE_2022Q1_FALSE_POSITIVE", "case_id": "C19_NATURE_2022_BRAND_EXPANSION_FAILED_RERATING", "symbol": "298540", "company_name": "더네이쳐홀딩스", "round": "R5", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "DOMESTIC_APPAREL_BRAND_EXPANSION_INVENTORY_RISK", "sector": "consumer_brand_distribution", "primary_archetype": "brand_retail_inventory_margin", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-05-16", "evidence_available_at_that_date": "Brand expansion narrative existed, but channel quality and inventory conversion were insufficient; price quickly told us the narrative was not a margin bridge.", "evidence_source": "historical quarterly earnings/channel inventory public evidence proxy; price rows from Songdaiki/stock-web", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "positioning_overheat"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/298/298540/2022.csv", "profile_path": "atlas/symbol_profiles/298/298540.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-05-16", "entry_price": 34700, "MFE_30D_pct": 1.7, "MFE_90D_pct": 1.7, "MFE_180D_pct": 1.7, "MFE_1Y_pct": 1.7, "MFE_2Y_pct": 1.7, "MAE_30D_pct": -25.6, "MAE_90D_pct": -25.6, "MAE_180D_pct": -43.8, "MAE_1Y_pct": -55.2, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-05-16", "peak_price": 35300, "drawdown_after_peak_pct": -55.2, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger", "four_b_evidence_type": ["margin_or_backlog_slowdown", "positioning_overheat"], "four_c_protection_label": null, "trigger_outcome_label": "failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2021-08_candidates", "same_entry_group_id": "SEG_298540_2022-05-16", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_C19_HANSAE_2022Q1_STAGE2_FALSE_POSITIVE", "case_id": "C19_HANSAE_2022_US_RETAIL_INVENTORY_DESTOCKING_4C", "symbol": "105630", "company_name": "한세실업", "round": "R5", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "APPAREL_OEM_RETAIL_INVENTORY_DESTOCKING_MARGIN_BREAK", "sector": "consumer_brand_distribution", "primary_archetype": "brand_retail_inventory_margin", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2022-05-16", "evidence_available_at_that_date": "Post-COVID apparel order recovery was overwhelmed by US retailer inventory destocking; the correct C19 lens is inventory/margin break, not simple order rebound.", "evidence_source": "historical quarterly earnings/channel inventory public evidence proxy; price rows from Songdaiki/stock-web", "stage2_evidence_fields": ["public_event_or_disclosure", "early_revision_signal"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "contract_delay"], "stage4c_evidence_fields": ["call_off_or_order_cut", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105630/2022.csv", "profile_path": "atlas/symbol_profiles/105/105630.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-05-16", "entry_price": 25800, "MFE_30D_pct": 0.8, "MFE_90D_pct": 0.8, "MFE_180D_pct": 0.8, "MFE_1Y_pct": 0.8, "MFE_2Y_pct": 0.8, "MAE_30D_pct": -35.9, "MAE_90D_pct": -40.3, "MAE_180D_pct": -42.1, "MAE_1Y_pct": -48.4, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-05-16", "peak_price": 26000, "drawdown_after_peak_pct": -48.4, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger", "four_b_evidence_type": ["margin_or_backlog_slowdown", "contract_delay"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "4C_success", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_105630_2022-05-16", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_C19_FILA_2021_REOPENING_PRICE_ONLY", "case_id": "C19_FILA_2021_BRAND_REOPENING_PRICE_ONLY_LOCAL_4B", "symbol": "081660", "company_name": "휠라홀딩스", "round": "R5", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "GLOBAL_SPORTS_BRAND_REOPENING_INVENTORY_OVERHANG", "sector": "consumer_brand_distribution", "primary_archetype": "brand_retail_inventory_margin", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage3-Yellow", "trigger_date": "2021-05-17", "evidence_available_at_that_date": "Reopening and brand-beta strength was visible, but no durable inventory/margin confirmation was present; local price peak alone should not become full 4B without non-price evidence.", "evidence_source": "historical quarterly earnings/channel inventory public evidence proxy; price rows from Songdaiki/stock-web", "stage2_evidence_fields": ["relative_strength", "public_event_or_disclosure"], "stage3_evidence_fields": ["multiple_public_sources"], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/081/081660/2021.csv", "profile_path": "atlas/symbol_profiles/081/081660.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-05-17", "entry_price": 55700, "MFE_30D_pct": 7.4, "MFE_90D_pct": 7.4, "MFE_180D_pct": 7.4, "MFE_1Y_pct": 7.4, "MFE_2Y_pct": 7.4, "MAE_30D_pct": -5.4, "MAE_90D_pct": -7.2, "MAE_180D_pct": -32.0, "MAE_1Y_pct": -37.5, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-06-03", "peak_price": 59800, "drawdown_after_peak_pct": -37.5, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_4B_trigger", "four_b_evidence_type": ["price_only_local_peak", "positioning_overheat"], "four_c_protection_label": null, "trigger_outcome_label": "4B_too_early", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_2018_candidate", "same_entry_group_id": "SEG_081660_2021-05-17", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "T_C19_FILA_2021_LOCAL_4B_PRICE_ONLY", "case_id": "C19_FILA_2021_BRAND_REOPENING_PRICE_ONLY_LOCAL_4B", "symbol": "081660", "company_name": "휠라홀딩스", "round": "R5", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "C19_OVERLAY", "sector": "consumer_brand_distribution", "primary_archetype": "brand_retail_inventory_margin", "loop_objective": "4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage4B", "trigger_date": "2021-06-03", "evidence_available_at_that_date": "local price peak near 2021-06-03 without non-price thesis break", "evidence_source": "historical price row plus non-price risk proxy", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/081/081660/2021.csv", "profile_path": "atlas/symbol_profiles/081/081660.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2021-06-03", "entry_price": 56800, "MFE_30D_pct": 5.3, "MFE_90D_pct": 5.3, "MFE_180D_pct": 5.3, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.2, "MAE_90D_pct": -12.5, "MAE_180D_pct": -33.8, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2021-06-03", "peak_price": 59800, "drawdown_after_peak_pct": -33.8, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 1.0, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only_local_peak", "positioning_overheat"], "four_c_protection_label": null, "trigger_outcome_label": "price_only_local_4B_too_early", "current_profile_verdict": "current_profile_4B_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_081660_2021-06-03", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": false, "reuse_reason": "overlay trigger for selected representative case", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
{"row_type": "trigger", "trigger_id": "T_C19_HANSAE_2022_4C_INVENTORY_DESTOCKING", "case_id": "C19_HANSAE_2022_US_RETAIL_INVENTORY_DESTOCKING_4C", "symbol": "105630", "company_name": "한세실업", "round": "R5", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "fine_archetype_id": "C19_OVERLAY", "sector": "consumer_brand_distribution", "primary_archetype": "brand_retail_inventory_margin", "loop_objective": "4B_non_price_requirement_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage4C", "trigger_date": "2022-05-19", "evidence_available_at_that_date": "inventory destocking route observed after initial recovery trigger", "evidence_source": "historical price row plus non-price risk proxy", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["call_off_or_order_cut", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/105/105630/2022.csv", "profile_path": "atlas/symbol_profiles/105/105630.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2022-05-19", "entry_price": 22700, "MFE_30D_pct": 2.0, "MFE_90D_pct": 2.0, "MFE_180D_pct": 2.0, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -27.1, "MAE_90D_pct": -32.2, "MAE_180D_pct": -35.7, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2022-05-20", "peak_price": 23150, "drawdown_after_peak_pct": -35.7, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "hard_4c_success", "four_b_evidence_type": ["margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "hard_4c_success", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "SEG_105630_2022-05-19", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": false, "reuse_reason": "overlay trigger for selected representative case", "independent_evidence_weight": 0.0, "do_not_count_as_new_case": true}
```
### 25.4 score_simulation rows
```jsonl
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C19_GAMSUNG_2023_SNOWPEAK_STORE_PRODUCTIVITY", "trigger_id": "T_C19_GAMSUNG_2023Q1_STAGE2_ACTIONABLE", "symbol": "036620", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 14, "revision_score": 18, "relative_strength_score": 16, "customer_quality_score": 12, "policy_or_regulatory_score": 0, "valuation_repricing_score": 10, "execution_risk_score": 4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 8, "inventory_turn_score": 10}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 18, "revision_score": 20, "relative_strength_score": 14, "customer_quality_score": 14, "policy_or_regulatory_score": 0, "valuation_repricing_score": 9, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 11, "inventory_turn_score": 13}, "weighted_score_after": 88, "stage_label_after": "Stage3-Green", "changed_components": ["inventory_turn_score", "margin_bridge_score", "execution_risk_score", "channel_reorder_score"], "component_delta_explanation": "C19 store productivity + inventory-turn confirmation lifts a genuine brand rerating above the generic Yellow ceiling.", "MFE_90D_pct": 56.8, "MAE_90D_pct": -4.9, "score_return_alignment_label": "aligned_after_shadow", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C19_FNF_2022_CHINA_BRAND_REORDER_HIGH_MAE_SUCCESS", "trigger_id": "T_C19_FNF_2022Q1_STAGE3_YELLOW", "symbol": "383220", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 15, "revision_score": 19, "relative_strength_score": 13, "customer_quality_score": 13, "policy_or_regulatory_score": 0, "valuation_repricing_score": 13, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 10, "inventory_turn_score": 8}, "weighted_score_before": 86, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 15, "revision_score": 18, "relative_strength_score": 11, "customer_quality_score": 13, "policy_or_regulatory_score": 0, "valuation_repricing_score": 11, "execution_risk_score": 9, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 10, "inventory_turn_score": 7}, "weighted_score_after": 82, "stage_label_after": "Stage3-Yellow", "changed_components": ["inventory_turn_score", "margin_bridge_score", "execution_risk_score", "channel_reorder_score"], "component_delta_explanation": "High-MAE apparel brand winners should stay Yellow until inventory risk is absorbed; do not force Green on reorder narrative alone.", "MFE_90D_pct": 25.2, "MAE_90D_pct": -9.0, "score_return_alignment_label": "mixed", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C19_NATURE_2022_BRAND_EXPANSION_FAILED_RERATING", "trigger_id": "T_C19_NATURE_2022Q1_FALSE_POSITIVE", "symbol": "298540", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 6, "revision_score": 9, "relative_strength_score": 17, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 12, "execution_risk_score": 15, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 4, "inventory_turn_score": 3}, "weighted_score_before": 73, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 3, "revision_score": 5, "relative_strength_score": 7, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 5, "execution_risk_score": 19, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 1, "inventory_turn_score": 0}, "weighted_score_after": 50, "stage_label_after": "Watch/No positive stage", "changed_components": ["inventory_turn_score", "margin_bridge_score", "execution_risk_score", "channel_reorder_score"], "component_delta_explanation": "C19 negative rule: brand store count or expansion headline without inventory-turn evidence caps at watchlist.", "MFE_90D_pct": 1.7, "MAE_90D_pct": -25.6, "score_return_alignment_label": "aligned_after_shadow", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C19_HANSAE_2022_US_RETAIL_INVENTORY_DESTOCKING_4C", "trigger_id": "T_C19_HANSAE_2022Q1_STAGE2_FALSE_POSITIVE", "symbol": "105630", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 6, "backlog_visibility_score": 7, "margin_bridge_score": 5, "revision_score": 11, "relative_strength_score": 12, "customer_quality_score": 7, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 18, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 3, "inventory_turn_score": 1}, "weighted_score_before": 72, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 2, "margin_bridge_score": 2, "revision_score": 4, "relative_strength_score": 4, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 3, "execution_risk_score": 24, "legal_or_contract_risk_score": 2, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 0, "inventory_turn_score": 0}, "weighted_score_after": 43, "stage_label_after": "4C/Thesis break", "changed_components": ["inventory_turn_score", "margin_bridge_score", "execution_risk_score", "channel_reorder_score"], "component_delta_explanation": "Inventory destocking evidence should route to 4C, not remain a Stage2 apparel recovery candidate.", "MFE_90D_pct": 0.8, "MAE_90D_pct": -40.3, "score_return_alignment_label": "aligned_after_shadow", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C19_FILA_2021_BRAND_REOPENING_PRICE_ONLY_LOCAL_4B", "trigger_id": "T_C19_FILA_2021_REOPENING_PRICE_ONLY", "symbol": "081660", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 7, "revision_score": 10, "relative_strength_score": 17, "customer_quality_score": 8, "policy_or_regulatory_score": 0, "valuation_repricing_score": 14, "execution_risk_score": 12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 3, "inventory_turn_score": 2}, "weighted_score_before": 73, "stage_label_before": "Stage2-Actionable/Yellow edge", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 5, "revision_score": 7, "relative_strength_score": 11, "customer_quality_score": 6, "policy_or_regulatory_score": 0, "valuation_repricing_score": 8, "execution_risk_score": 17, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "channel_reorder_score": 1, "inventory_turn_score": 0}, "weighted_score_after": 55, "stage_label_after": "Watch + 4B overlay only", "changed_components": ["inventory_turn_score", "margin_bridge_score", "execution_risk_score", "channel_reorder_score"], "component_delta_explanation": "Existing price-only blowoff guard is strengthened for C19: local price peak is overlay only unless inventory/margin deterioration is visible.", "MFE_90D_pct": 7.4, "MAE_90D_pct": -7.2, "score_return_alignment_label": "aligned_after_shadow", "current_profile_verdict": "current_profile_4B_too_early"}
```
### 25.5 shadow_weight rows
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C19_inventory_turn_required_for_Green,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1,"Brand/store expansion must convert to inventory turn and margin bridge before Green","reduced false positives in 298540/105630/081660 while retaining 036620","T_C19_GAMSUNG_2023Q1_STAGE2_ACTIONABLE|T_C19_NATURE_2022Q1_FALSE_POSITIVE|T_C19_HANSAE_2022Q1_STAGE2_FALSE_POSITIVE|T_C19_FILA_2021_REOPENING_PRICE_ONLY",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C19_price_only_relative_strength_cap,canonical_archetype_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,false,true,+1,"Reopening/brand beta without sell-through evidence cannot promote Stage3","blocks price-only local 4B/false-positive entries",T_C19_FILA_2021_LOCAL_4B_PRICE_ONLY|T_C19_NATURE_2022Q1_FALSE_POSITIVE,5,5,3,medium,canonical_shadow_only,"strengthens existing price-only blowoff guard"
shadow_weight,L5_execution_risk_penalty_inventory_destocking,sector_specific,L5_CONSUMER_BRAND_DISTRIBUTION,C19_BRAND_RETAIL_INVENTORY_MARGIN,0,1,+1,"Retailer inventory destocking is a thesis-break route, not a normal pullback","routes 105630 to 4C earlier",T_C19_HANSAE_2022_4C_INVENTORY_DESTOCKING,5,5,3,low,sector_shadow_only,"requires more R5 holdout before production"
```
### 25.6 residual_contribution row
```jsonl
{"row_type": "residual_contribution", "round": "R5", "loop": "15", "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "scheduled_round": "R5", "scheduled_loop": 15, "round_schedule_status": "valid", "round_sector_consistency": "pass", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "same_archetype_new_symbol_count": 5, "same_archetype_new_trigger_family_count": 5, "new_trigger_family_count": 5, "positive_case_count": 2, "counterexample_count": 3, "current_profile_error_count": 4, "tested_existing_calibrated_axes": ["price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "stage3_green_revision_min"], "residual_error_types_found": ["brand_expansion_without_inventory_turn_false_positive", "retailer_destocking_4C_route", "price_only_reopening_beta_local_4B"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false, "diversity_score_summary": "5 new C19 symbols and 5 trigger families; no reused representative cases; counterexample-heavy to avoid another C20 repeat."}
```
### 25.7 narrative_only rows
```jsonl
{"row_type": "narrative_only", "case_id": "NONE", "symbol": null, "large_sector_id": "L5_CONSUMER_BRAND_DISTRIBUTION", "canonical_archetype_id": "C19_BRAND_RETAIL_INVENTORY_MARGIN", "reason": "all selected representative cases have usable 180D windows", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
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
completed_loop = 15
next_round = R6
next_loop = 15
round_schedule_status = valid
round_sector_consistency = pass
```
## 28. Source Notes
- Stock-Web manifest was read from `atlas/manifest.json`; manifest `max_date` is `2026-02-20`, price basis is `tradable_raw`, and price adjustment status is `raw_unadjusted_marcap`.
- Symbol profiles checked: `036620`, `383220`, `298540`, `105630`, `081660`. All selected windows are outside corporate-action-contaminated 180D windows.
- Representative OHLC rows were read from the listed tradable yearly CSV shards. Raw shards were not used for weight calibration.

