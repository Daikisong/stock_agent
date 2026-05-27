# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
round = R2
loop = 11
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id = TEST_SOCKET_CUSTOMER_QUALITY_DESIGN_WIN_VS_SOCKET_BETA_FALSE_GREEN
output_file = e2r_stock_web_v12_residual_round_R2_loop_11_L2_AI_SEMICONDUCTOR_ELECTRONICS_C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY_research.md
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
stock_agent_live_scan_allowed = false
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_embedded = true
handoff_prompt_executed_now = false
```

This MD is historical calibration research only. It is not live candidate discovery, not an investment recommendation, not a repository patch, and not a production scoring change.

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

Existing global axes are treated as already applied. This loop does not re-propose them globally. It stress-tests the C08 socket/test-customer-quality branch and proposes only shadow sector/archetype rules.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| round | R2 |
| loop | 11 |
| sector | AI·반도체·전자부품 |
| large_sector_id | L2_AI_SEMICONDUCTOR_ELECTRONICS |
| canonical_archetype_id | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY |
| fine_archetype_id | TEST_SOCKET_CUSTOMER_QUALITY_DESIGN_WIN_VS_SOCKET_BETA_FALSE_GREEN |
| loop_objective | counterexample_mining; green_strictness_stress_test; 4B_non_price_requirement_stress_test; sector_specific_rule_discovery; canonical_archetype_compression; coverage_gap_fill |

## 3. Previous Coverage / Duplicate Avoidance Check

Accessible calibration artifacts show the previous ingest snapshot covered R1~R13 and loops 1~9, with 4,951 raw trigger rows, 1,940 validated trigger rows, and 1,376 aggregate representative rows. The applied global scoring diff already promoted Stage2 evidence bonus, stricter Green, Green revision confirmation, and 4B/4C guardrails.

This loop therefore avoids:
- re-proving that Stage2 is earlier than Green,
- re-proving that price-only 4B is insufficient,
- reusing the standard R1/R2 HBM/power/defense set,
- treating socket/HBM beta as Green without customer-specific and revision evidence.

Novelty target: same R2 sector, but non-HBM-test-socket customer-quality residual.

## 4. Stock-Web OHLC Input / Price Source Validation

```json
{
  "row_type": "price_source_validation",
  "source": "Songdaiki/stock-web",
  "source_url": "https://github.com/Songdaiki/stock-web",
  "manifest_path": "atlas/manifest.json",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv",
  "manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "validation_status": "usable_for_historical_calibration"
}
```

Manifest fields checked:

| field | value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14,354,401 |
| raw_row_count | 15,214,118 |
| symbol_count | 5,414 |
| active_like_symbol_count | 2,868 |
| inactive_or_delisted_like_symbol_count | 2,546 |
| markets | KONEX; KOSDAQ; KOSDAQ GLOBAL; KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Schema fields checked: tradable columns `d,o,h,l,c,v,a,mc,s,m`; raw columns add `rs`; MFE/MAE formula uses max high/min low from entry through N tradable rows.

## 5. Historical Eligibility Gate

| symbol | company | entry | 180D forward available | corporate-action 180D overlap | calibration_usable |
|---|---:|---:|---:|---:|---:|
| 058470 | 리노공업 | 2024-03-08 | yes | no | true |
| 095340 | ISC | 2024-03-08 | yes | no | true |
| 131290 | 티에스이 | 2024-04-24 | yes | no | true |

Notes:
- 리노공업 profile has a 2025-04-25 corporate-action candidate, so 2Y is blocked/contaminated-or-unavailable for this research window. 180D and 1Y fields are still usable because the representative 180D/1Y windows end before that event.
- ISC has a 2023-10-20 corporate-action candidate outside the selected 2024 windows.
- 티에스이 corporate-action candidates are from 2011 and outside all tested windows.

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine_archetype_id | compressed mechanism |
|---|---|---|
| C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | TEST_SOCKET_CUSTOMER_QUALITY_DESIGN_WIN_VS_SOCKET_BETA_FALSE_GREEN | Customer-specific test socket / probe card / test-interface evidence must be separated from generalized AI/HBM socket beta. A customer-quality bridge can support Stage2/Yellow; Green requires realized margin/revision or repeated customer conversion. |

## 7. Case Selection Summary

| case_id | symbol | company | case role | positive/counterexample | new independent? | reason |
|---|---:|---|---|---|---:|---|
| R2L11_C08_058470_LINO_20240308 | 058470 | 리노공업 | structural_success | positive | true | customer-quality socket exposure + relative strength worked, but Green would be late |
| R2L11_C08_095340_ISC_20240308 | 095340 | ISC | false_positive_green | counterexample | true | socket/HBM beta spiked, then failed the 180D path |
| R2L11_C08_131290_TSE_20240424 | 131290 | 티에스이 | high_mae_success | positive | true | Stage2 worked, but Green without repeated customer/revision evidence suffered high MAE |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
calibration_usable_case_count = 3
calibration_usable_trigger_count = 5
representative_trigger_count = 3
new_independent_case_ratio = 1.00
counterexample_search_incomplete = false
do_not_propose_global_delta = true
```

This is sufficient for a C08-specific shadow candidate, not for a global rule.

## 9. Evidence Source Map

| evidence family | Stage2 use | Stage3 use | 4B/4C use |
|---|---|---|---|
| relative_strength | allowed only with non-price socket/customer narrative | insufficient alone for Green | can flag overheat but not full 4B alone |
| customer_or_order_quality | C08 core bridge | must become durable customer confirmation/repeat order | deterioration can become 4B/4C watch |
| early_revision_signal | Stage2 bonus eligible | Green requires stronger revision/margin bridge | revision slowdown supports 4B |
| margin_bridge | weak at Stage2 | required for Green in proposed C08 branch | margin miss turns into 4C watch |
| price_only_local_peak | not positive evidence | not positive evidence | local 4B watch only unless non-price evidence exists |

## 10. Price Data Source Map

| symbol | profile_path | representative shard | extra shard |
|---|---|---|---|
| 058470 | atlas/symbol_profiles/058/058470.json | atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv | atlas/ohlcv_tradable_by_symbol_year/058/058470/2025.csv |
| 095340 | atlas/symbol_profiles/095/095340.json | atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv | atlas/ohlcv_tradable_by_symbol_year/095/095340/2025.csv |
| 131290 | atlas/symbol_profiles/131/131290.json | atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv | atlas/ohlcv_tradable_by_symbol_year/131/131290/2025.csv |

## 11. Case-by-Case Trigger Grid

| trigger_id | company | type | trigger_date | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | current verdict | aggregate role |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| R2L11_C08_058470_STAGE2_20240308 | 리노공업 | Stage2-Actionable | 2024-03-08 | 2024-03-08 | 215,500 | 31.09 | 43.39 | 43.39 | -6.96 | -6.96 | -33.5 | current_profile_correct | representative |
| R2L11_C08_058470_GREEN_20240412 | 리노공업 | Stage3-Green | 2024-04-12 | 2024-04-12 | 274,500 | 12.57 | 12.57 | 12.57 | -9.65 | -40.26 | -47.8 | current_profile_too_late | label_comparison_only |
| R2L11_C08_095340_GREENFALSE_20240308 | ISC | Stage3-Green-candidate | 2024-03-08 | 2024-03-08 | 95,000 | 13.68 | 13.68 | 13.68 | -12.63 | -43.16 | -52.95 | current_profile_false_positive | representative |
| R2L11_C08_131290_STAGE2_20240424 | 티에스이 | Stage2-Actionable | 2024-04-24 | 2024-04-24 | 64,200 | 36.76 | 36.76 | 36.76 | -12.93 | -40.73 | -45.48 | current_profile_too_early | representative |
| R2L11_C08_131290_GREEN_20240426 | 티에스이 | Stage3-Green-candidate | 2024-04-26 | 2024-04-26 | 79,000 | 11.14 | 11.14 | 11.14 | -29.24 | -51.84 | -55.7 | current_profile_too_early | label_comparison_only |

## 12. Trigger-Level OHLC Backtest Tables

### 12.1 Representative aggregate triggers

| case | entry | entry_price | peak_date | peak_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | drawdown_after_peak | outcome |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 리노공업 | 2024-03-08 | 215,500 | 2024-05-07 | 309,000 | 31.09 | 43.39 | 43.39 | -6.96 | -6.96 | -33.50 | -53.62 | success but requires 4B/high-MAE watch |
| ISC | 2024-03-08 | 95,000 | 2024-03-28 | 108,000 | 13.68 | 13.68 | 13.68 | -12.63 | -43.16 | -52.95 | -58.61 | false Green / socket beta failure |
| 티에스이 | 2024-04-24 | 64,200 | 2024-05-03 | 87,800 | 36.76 | 36.76 | 36.76 | -12.93 | -40.73 | -45.48 | -60.14 | Stage2 success, Green high-MAE failure |

### 12.2 Label comparison triggers

| case | comparison trigger | entry | entry_price | MFE90 | MAE90 | green_lateness_ratio | verdict |
|---|---|---|---:|---:|---:|---:|---|
| 리노공업 | Stage3-Green comparison | 2024-04-12 | 274,500 | 12.57 | -40.26 | 0.63 | Green caught too much of the move late |
| 티에스이 | Stage3-Green candidate | 2024-04-26 | 79,000 | 11.14 | -51.84 | 0.63 | follow-through spike was not durable enough for Green |

## 13. Current Calibrated Profile Stress Test

| case | current profile likely action | actual path | profile verdict | axis tested |
|---|---|---|---|---|
| 리노공업 | Stage2/Yellow first, Green after revision evidence | 43.39% MFE180 but -33.50% MAE180 | current_profile_correct | stage3_green_revision_min kept |
| ISC | Could over-score as Green if socket/HBM beta + RS are treated as customer quality | only 13.68% MFE180 vs -52.95% MAE180 | current_profile_false_positive | Green strictness must be C08-specific |
| 티에스이 | Stage2 is valid; Green too early if order burst is over-weighted | 36.76% MFE180 but -45.48% MAE180 | current_profile_too_early | high-MAE guard needed |

Answers to required stress-test questions:
1. Current calibrated profile is broadly correct for Stage2/Yellow but still vulnerable to C08 false Green when relative strength is mistaken for durable customer quality.
2. The profile is aligned for 리노공업, false-positive for ISC, and too early for 티에스이 Green.
3. Stage2 bonus is not excessive if evidence is non-price and customer-specific; it is excessive if the only bridge is socket beta.
4. Yellow 75 remains useful as an intermediate label.
5. Green 87 / revision 55 should be strengthened only inside C08 customer-quality branch.
6. Price-only blowoff guard is appropriate.
7. Full 4B non-price requirement is appropriate; local price peaks alone created false exits.
8. Hard 4C routing is not weakened; C08 cases mostly need watch/guard before hard 4C.

## 14. Stage2 / Yellow / Green Comparison

| case | Stage2 entry | Green comparison entry | peak after Stage2 | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| 리노공업 | 215,500 | 274,500 | 309,000 | 0.63 | Green misses most of the Stage2-to-peak upside |
| ISC | 95,000 | not valid Green | 108,000 | not_applicable | Green should be capped because customer/revision bridge failed |
| 티에스이 | 64,200 | 79,000 | 87,800 | 0.63 | Green candidate was a high-MAE late follow-through |

## 15. 4B Local vs Full-window Timing Audit

| case | local peak | full observed peak | local proximity | full-window proximity | evidence type | verdict |
|---|---:|---:|---:|---:|---|---|
| 리노공업 | 309,000 | 309,000 | n/a | n/a | none at Stage2 | later 4B watch needed, not entry row |
| ISC | 108,000 | 108,000 | 0.91 | 0.91 | price_only; valuation_blowoff; positioning_overheat | price-only local 4B was not enough; Green should be capped first |
| 티에스이 | 87,800 | 87,800 | 0.63 | 0.63 | price_only; positioning_overheat | watch only, not full 4B without non-price deterioration |

## 16. 4C Protection Audit

| case | 4C label | reason |
|---|---|---|
| 리노공업 | thesis_break_watch_only | drawdown severe, but no hard thesis-break evidence in this research row |
| ISC | thesis_break_watch_only | large MAE suggests false Green guard rather than immediate hard 4C |
| 티에스이 | thesis_break_watch_only | high MAE after order spike; needs repeated customer/revision failure to become hard 4C |

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
axis = c08_green_requires_realized_customer_quality_and_revision
baseline_value = false
tested_value = true
delta = +1 C08-specific guard
proposal_type = sector_shadow_only
confidence = low_to_medium
```

Reason: In R2 test-socket/probe-interface names, relative strength and AI/HBM socket beta can generate fast MFE, but without durable customer quality and revision/margin bridge, the 90D/180D MAE can swamp the signal.

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
new_axis_proposed:
  - c08_customer_specific_design_win_bridge_bonus
  - c08_socket_beta_green_cap_without_realized_revision
  - c08_socket_momentum_high_mae_guard
```

Interpretation:
- Customer-specific design-win / confirmed customer-quality evidence can support Stage2-Actionable or Yellow.
- Green should require realized revision, margin bridge, or repeated customer conversion.
- If first MFE is large but MAE_90D < -30%, the case should be tagged high-MAE success and routed to 4B/watch, not used as clean Green evidence.

## 19. Before / After Backtest Comparison

| profile | scope | eligible representative triggers | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | missed_structural_count | late_green_count | alignment verdict |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | 3 | 31.28 | -30.28 | 31.28 | -43.98 | 0.33 | 0 | 2 | partially aligned; C08 false Green remains |
| P0b e2r_2_0_baseline_reference | rollback | 3 | 31.28 | -30.28 | 31.28 | -43.98 | 0.67 | 0 | 1 | too permissive for Green |
| P1 sector_specific_candidate_profile | L2 | 3 | 31.28 | -30.28 | 31.28 | -43.98 | 0.00 | 0 | 2 | better C08 risk labeling |
| P2 canonical_archetype_candidate_profile | C08 | 3 | 31.28 | -30.28 | 31.28 | -43.98 | 0.00 | 0 | 2 | best explanatory fit |
| P3 counterexample_guard_profile | C08 guard | 3 | 31.28 | -30.28 | 31.28 | -43.98 | 0.00 | 0 | 2 | caps ISC-style false Green |

## 20. Score-Return Alignment Matrix

| case | before score/stage | after shadow score/stage | return alignment |
|---|---|---|---|
| 리노공업 | 78 / Stage3-Yellow | 84 / Stage3-Yellow-plus | aligned positive, but Green late |
| ISC | 82 / Stage3-Green-candidate | 70 / Stage2-Yellow capped | false positive reduced |
| 티에스이 | 77 / Stage3-Yellow | 70 / Stage2-Actionable capped | high-MAE success no longer treated as clean Green |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | TEST_SOCKET_CUSTOMER_QUALITY_DESIGN_WIN_VS_SOCKET_BETA_FALSE_GREEN | 2 | 1 | 1 | 0 | 3 | 0 | 5 | 3 | 2 | true | true | C08 now has positive + false Green + high-MAE success sample; needs holdout validation |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
same_archetype_new_symbol_count: 3
same_archetype_new_trigger_family_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage3_green_revision_min
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage
residual_error_types_found:
  - false_positive_green
  - high_mae_success
  - green_lateness_in_customer_quality_socket
new_axis_proposed:
  - c08_customer_specific_design_win_bridge_bonus
  - c08_socket_beta_green_cap_without_realized_revision
  - c08_socket_momentum_high_mae_guard
existing_axis_strengthened:
  - stage3_green_revision_min in C08 only
  - full_4b_requires_non_price_evidence in C08 only
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
diversity_score_summary: high_total_57_avg_19.0
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:
- stock-web manifest/schema fields,
- symbol profile availability,
- representative 2024/2025 tradable shard rows,
- entry_date / entry_price,
- MFE/MAE 30D/90D/180D,
- current calibrated profile stress-test as research proxy.

Not validated:
- live current candidate state,
- brokerage data,
- production score code,
- actual repository implementation,
- full source-document audit for every historical disclosure timestamp.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c08_green_requires_realized_customer_quality_and_revision,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"C08 false Green appears when socket/HBM beta and RS are treated as durable customer quality","ISC false Green capped; TSE high-MAE Green capped","R2L11_C08_095340_GREENFALSE_20240308|R2L11_C08_131290_STAGE2_20240424",3,3,1,low_to_medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,c08_customer_specific_design_win_bridge_bonus,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"Customer-specific design-win/quality evidence can justify Stage2/Yellow earlier than revision-confirmed Green","Lino-type Stage2 preserved without relaxing Green globally","R2L11_C08_058470_STAGE2_20240308",3,3,1,low,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,c08_socket_momentum_high_mae_guard,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"Large early MFE with MAE90 below -30% should be tagged high-MAE success/watch rather than clean Green","TSE path moved to Stage2/Yellow plus 4B watch","R2L11_C08_131290_STAGE2_20240424",3,3,1,low_to_medium,archetype_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows

```jsonl
{"row_type":"case","case_id":"R2L11_C08_058470_LINO_20240308","symbol":"058470","company_name":"리노공업","round":"R2","loop":"11","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_DESIGN_WIN_VS_SOCKET_BETA_FALSE_GREEN","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"R2L11_C08_058470_STAGE2_20240308","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Stage2/Yellow was aligned; Green confirmation would be late after much of the upside.","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Customer-quality socket exposure and relative strength worked, but later drawdown shows this archetype needs 4B/high-MAE watch once valuation and positioning overheat."}
{"row_type":"case","case_id":"R2L11_C08_095340_ISC_20240308","symbol":"095340","company_name":"ISC","round":"R2","loop":"11","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_DESIGN_WIN_VS_SOCKET_BETA_FALSE_GREEN","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R2L11_C08_095340_GREENFALSE_20240308","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Socket/HBM beta had headline strength but did not close the customer-quality + realized revision bridge; 180D drawdown dominated.","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Useful residual counterexample: strong relative strength and narrative cannot substitute for durable customer qualification and confirmed revision."}
{"row_type":"case","case_id":"R2L11_C08_131290_TSE_20240424","symbol":"131290","company_name":"티에스이","round":"R2","loop":"11","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_DESIGN_WIN_VS_SOCKET_BETA_FALSE_GREEN","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R2L11_C08_131290_STAGE2_20240424","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Stage2 was tradable, but Green after the first order/relative-strength spike was not sufficiently protected from high MAE.","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"Positive MFE exists, but path quality is poor; C08 should promote Stage2/Yellow while holding Green for customer-specific, repeated, margin-confirmed evidence."}
```

### 25.3 trigger rows

```jsonl
{"round":"R2","loop":"11","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_DESIGN_WIN_VS_SOCKET_BETA_FALSE_GREEN","sector":"AI·반도체·전자부품","primary_archetype":"semi test socket customer quality","loop_objective":"counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"row_type":"trigger","trigger_id":"R2L11_C08_058470_STAGE2_20240308","case_id":"R2L11_C08_058470_LINO_20240308","symbol":"058470","company_name":"리노공업","trigger_type":"Stage2-Actionable","trigger_date":"2024-03-08","entry_date":"2024-03-08","entry_price":215500,"evidence_available_at_that_date":"Relative-strength breakout plus public AI/on-device semiconductor socket demand narrative; customer quality inferred but not yet fully revision-confirmed.","evidence_source":"public market/report narrative proxy; point-in-time research proxy, not live recommendation","stage2_evidence_fields":["relative_strength","customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv","profile_path":"atlas/symbol_profiles/058/058470.json","MFE_30D_pct":31.09,"MFE_90D_pct":43.39,"MFE_180D_pct":43.39,"MFE_1Y_pct":43.39,"MFE_2Y_pct":null,"MAE_30D_pct":-6.96,"MAE_90D_pct":-6.96,"MAE_180D_pct":-33.5,"MAE_1Y_pct":-33.5,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-07","peak_price":309000,"drawdown_after_peak_pct":-53.62,"green_lateness_ratio":0.63,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_stage2_representative","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"structural_success_with_high_mae_after_peak","current_profile_verdict":"current_profile_correct","corporate_action_window_status":"clean_180D_window; 2Y blocked by 2025-04-25 corporate-action candidate","same_entry_group_id":"058470_2024-03-08_215500","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"round":"R2","loop":"11","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_DESIGN_WIN_VS_SOCKET_BETA_FALSE_GREEN","sector":"AI·반도체·전자부품","primary_archetype":"semi test socket customer quality","loop_objective":"counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"row_type":"trigger","trigger_id":"R2L11_C08_058470_GREEN_20240412","case_id":"R2L11_C08_058470_LINO_20240308","symbol":"058470","company_name":"리노공업","trigger_type":"Stage3-Green","trigger_date":"2024-04-12","entry_date":"2024-04-12","entry_price":274500,"evidence_available_at_that_date":"Follow-through strength after March breakout; research proxy treats this as Green comparison only, not representative entry.","evidence_source":"public market/report narrative proxy; point-in-time research proxy","stage2_evidence_fields":["relative_strength","customer_or_order_quality"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv","profile_path":"atlas/symbol_profiles/058/058470.json","MFE_30D_pct":12.57,"MFE_90D_pct":12.57,"MFE_180D_pct":12.57,"MFE_1Y_pct":12.57,"MFE_2Y_pct":null,"MAE_30D_pct":-9.65,"MAE_90D_pct":-40.26,"MAE_180D_pct":-47.8,"MAE_1Y_pct":-47.8,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-07","peak_price":309000,"drawdown_after_peak_pct":-53.62,"green_lateness_ratio":0.63,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"label_comparison_green_late","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"late_green_high_mae","current_profile_verdict":"current_profile_too_late","corporate_action_window_status":"clean_180D_window; 2Y blocked by 2025-04-25 corporate-action candidate","same_entry_group_id":"058470_2024-04-12_274500","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":false,"reuse_reason":"same_case_green_comparison","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
{"round":"R2","loop":"11","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_DESIGN_WIN_VS_SOCKET_BETA_FALSE_GREEN","sector":"AI·반도체·전자부품","primary_archetype":"semi test socket customer quality","loop_objective":"counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"row_type":"trigger","trigger_id":"R2L11_C08_095340_GREENFALSE_20240308","case_id":"R2L11_C08_095340_ISC_20240308","symbol":"095340","company_name":"ISC","trigger_type":"Stage3-Green-candidate","trigger_date":"2024-03-08","entry_date":"2024-03-08","entry_price":95000,"evidence_available_at_that_date":"Socket/HBM beta and strong one-day breakout; customer-quality and realized revision bridge not yet durable enough for Green.","evidence_source":"public market/report narrative proxy; point-in-time research proxy","stage2_evidence_fields":["relative_strength","customer_or_order_quality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv","profile_path":"atlas/symbol_profiles/095/095340.json","MFE_30D_pct":13.68,"MFE_90D_pct":13.68,"MFE_180D_pct":13.68,"MFE_1Y_pct":13.68,"MFE_2Y_pct":null,"MAE_30D_pct":-12.63,"MAE_90D_pct":-43.16,"MAE_180D_pct":-52.95,"MAE_1Y_pct":-52.95,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-28","peak_price":108000,"drawdown_after_peak_pct":-58.61,"green_lateness_ratio":"not_applicable_false_green","four_b_local_peak_proximity":0.91,"four_b_full_window_peak_proximity":0.91,"four_b_timing_verdict":"price_only_local_4B_too_early_without_revision_confirmation","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"false_positive_green_high_drawdown","current_profile_verdict":"current_profile_false_positive","corporate_action_window_status":"clean_180D_window; prior 2023-10-20 corporate-action candidate outside window","same_entry_group_id":"095340_2024-03-08_95000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"round":"R2","loop":"11","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_DESIGN_WIN_VS_SOCKET_BETA_FALSE_GREEN","sector":"AI·반도체·전자부품","primary_archetype":"semi test socket customer quality","loop_objective":"counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"row_type":"trigger","trigger_id":"R2L11_C08_131290_STAGE2_20240424","case_id":"R2L11_C08_131290_TSE_20240424","symbol":"131290","company_name":"티에스이","trigger_type":"Stage2-Actionable","trigger_date":"2024-04-24","entry_date":"2024-04-24","entry_price":64200,"evidence_available_at_that_date":"Probe/test-interface order and relative-strength burst; Stage2 entry, not yet Green without repeated customer conversion and margin confirmation.","evidence_source":"public market/report narrative proxy; point-in-time research proxy","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","customer_or_order_quality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv","profile_path":"atlas/symbol_profiles/131/131290.json","MFE_30D_pct":36.76,"MFE_90D_pct":36.76,"MFE_180D_pct":36.76,"MFE_1Y_pct":36.76,"MFE_2Y_pct":null,"MAE_30D_pct":-12.93,"MAE_90D_pct":-40.73,"MAE_180D_pct":-45.48,"MAE_1Y_pct":-45.48,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-03","peak_price":87800,"drawdown_after_peak_pct":-60.14,"green_lateness_ratio":0.63,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable_stage2_representative","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"high_mae_success_stage2_only","current_profile_verdict":"current_profile_too_early","corporate_action_window_status":"clean_180D_window","same_entry_group_id":"131290_2024-04-24_64200","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"round":"R2","loop":"11","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"TEST_SOCKET_CUSTOMER_QUALITY_DESIGN_WIN_VS_SOCKET_BETA_FALSE_GREEN","sector":"AI·반도체·전자부품","primary_archetype":"semi test socket customer quality","loop_objective":"counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|sector_specific_rule_discovery|canonical_archetype_compression|coverage_gap_fill","price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"row_type":"trigger","trigger_id":"R2L11_C08_131290_GREEN_20240426","case_id":"R2L11_C08_131290_TSE_20240424","symbol":"131290","company_name":"티에스이","trigger_type":"Stage3-Green-candidate","trigger_date":"2024-04-26","entry_date":"2024-04-26","entry_price":79000,"evidence_available_at_that_date":"Follow-through two days after Stage2 burst; used as Green comparison only because customer/revision bridge remained incomplete.","evidence_source":"public market/report narrative proxy; point-in-time research proxy","stage2_evidence_fields":["public_event_or_disclosure","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv","profile_path":"atlas/symbol_profiles/131/131290.json","MFE_30D_pct":11.14,"MFE_90D_pct":11.14,"MFE_180D_pct":11.14,"MFE_1Y_pct":11.14,"MFE_2Y_pct":null,"MAE_30D_pct":-29.24,"MAE_90D_pct":-51.84,"MAE_180D_pct":-55.7,"MAE_1Y_pct":-55.7,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-03","peak_price":87800,"drawdown_after_peak_pct":-60.14,"green_lateness_ratio":0.63,"four_b_local_peak_proximity":0.63,"four_b_full_window_peak_proximity":0.63,"four_b_timing_verdict":"price_only_local_4B_watch_not_full_4B","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"green_candidate_late_and_high_mae","current_profile_verdict":"current_profile_too_early","corporate_action_window_status":"clean_180D_window","same_entry_group_id":"131290_2024-04-26_79000","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":false,"reuse_reason":"same_case_green_comparison","independent_evidence_weight":0.0,"do_not_count_as_new_case":true}
```

### 25.4 score_simulation rows

```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L11_C08_058470_LINO_20240308","trigger_id":"R2L11_C08_058470_STAGE2_20240308","symbol":"058470","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":2,"backlog_visibility_score":1,"margin_bridge_score":6,"revision_score":52,"relative_strength_score":84,"customer_quality_score":76,"policy_or_regulatory_score":0,"valuation_repricing_score":62,"execution_risk_score":25,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":45,"order_intake_quality_score":50},"weighted_score_before":78,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":2,"backlog_visibility_score":1,"margin_bridge_score":6,"revision_score":56,"relative_strength_score":84,"customer_quality_score":84,"policy_or_regulatory_score":0,"valuation_repricing_score":62,"execution_risk_score":30,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":45,"order_intake_quality_score":50},"weighted_score_after":84,"stage_label_after":"Stage3-Yellow-plus","changed_components":["customer_quality_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C08 shadow profile rewards customer-specific quality/design-win evidence, but caps Green when realized revision/margin bridge is weak or when execution/valuation risk dominates.","MFE_90D_pct":43.39,"MAE_90D_pct":-6.96,"score_return_alignment_label":"aligned_positive_but_green_late","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L11_C08_095340_ISC_20240308","trigger_id":"R2L11_C08_095340_GREENFALSE_20240308","symbol":"095340","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":38,"relative_strength_score":90,"customer_quality_score":46,"policy_or_regulatory_score":0,"valuation_repricing_score":70,"execution_risk_score":55,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":35,"order_intake_quality_score":30},"weighted_score_before":82,"stage_label_before":"Stage3-Green-candidate","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":30,"relative_strength_score":90,"customer_quality_score":36,"policy_or_regulatory_score":0,"valuation_repricing_score":55,"execution_risk_score":70,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":35,"order_intake_quality_score":30},"weighted_score_after":70,"stage_label_after":"Stage2/Yellow-capped","changed_components":["customer_quality_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C08 shadow profile rewards customer-specific quality/design-win evidence, but caps Green when realized revision/margin bridge is weak or when execution/valuation risk dominates.","MFE_90D_pct":13.68,"MAE_90D_pct":-43.16,"score_return_alignment_label":"misaligned_false_positive_before_guard","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L11_C08_131290_TSE_20240424","trigger_id":"R2L11_C08_131290_STAGE2_20240424","symbol":"131290","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":4,"backlog_visibility_score":1,"margin_bridge_score":4,"revision_score":42,"relative_strength_score":86,"customer_quality_score":54,"policy_or_regulatory_score":0,"valuation_repricing_score":58,"execution_risk_score":45,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":55,"order_intake_quality_score":68},"weighted_score_before":77,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":4,"backlog_visibility_score":1,"margin_bridge_score":4,"revision_score":35,"relative_strength_score":86,"customer_quality_score":48,"policy_or_regulatory_score":0,"valuation_repricing_score":58,"execution_risk_score":65,"legal_or_contract_risk_score":5,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":55,"order_intake_quality_score":60},"weighted_score_after":70,"stage_label_after":"Stage2-Actionable-capped","changed_components":["customer_quality_score","revision_score","execution_risk_score","valuation_repricing_score"],"component_delta_explanation":"C08 shadow profile rewards customer-specific quality/design-win evidence, but caps Green when realized revision/margin bridge is weak or when execution/valuation risk dominates.","MFE_90D_pct":36.76,"MAE_90D_pct":-40.73,"score_return_alignment_label":"high_mae_success_requires_guard","current_profile_verdict":"current_profile_too_early"}
```

### 25.5 shadow_weight rows

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c08_green_requires_realized_customer_quality_and_revision,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"C08 false Green appears when socket/HBM beta and RS are treated as durable customer quality","ISC false Green capped; TSE high-MAE Green capped","R2L11_C08_095340_GREENFALSE_20240308|R2L11_C08_131290_STAGE2_20240424",3,3,1,low_to_medium,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,c08_customer_specific_design_win_bridge_bonus,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"Customer-specific design-win/quality evidence can justify Stage2/Yellow earlier than revision-confirmed Green","Lino-type Stage2 preserved without relaxing Green globally","R2L11_C08_058470_STAGE2_20240308",3,3,1,low,archetype_shadow_only,"not production; post-calibrated residual"
shadow_weight,c08_socket_momentum_high_mae_guard,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"Large early MFE with MAE90 below -30% should be tagged high-MAE success/watch rather than clean Green","TSE path moved to Stage2/Yellow plus 4B watch","R2L11_C08_131290_STAGE2_20240424",3,3,1,low_to_medium,archetype_shadow_only,"not production; post-calibrated residual"
```

### 25.6 residual_contribution row

```jsonl
{"row_type":"residual_contribution","round":"R2","loop":"11","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"same_archetype_new_symbol_count":3,"same_archetype_new_trigger_family_count":3,"new_canonical_archetype_count":0,"new_trigger_family_count":3,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":2,"diversity_score_summary":"high_total_57_avg_19.0","tested_existing_calibrated_axes":["stage3_green_revision_min","full_4b_requires_non_price_evidence","price_only_blowoff_blocks_positive_stage"],"residual_error_types_found":["false_positive_green","high_mae_success","green_lateness_in_customer_quality_socket"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"R2/C08 undercovered non-HBM test-socket customer-quality residual; adds customer-quality positive, socket-beta false Green, and high-MAE success guard."}
```

### 25.7 narrative_only rows

```jsonl
{"row_type":"narrative_only","case_id":"R2L11_C08_FUTURE_HOLDOUT","symbol":"000000","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","reason":"holdout validation still needed for additional non-HBM socket/test names and later-cycle 4C examples","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown files are v12 post-calibrated residual research outputs produced using the Songdaiki/stock-web OHLC atlas.

These MDs are not live candidate research. They are historical calibration research designed to extend the already-applied e2r_2_1_stock_web_calibrated profile.

Do not blindly apply every shadow row.
Ingest the machine-readable rows and update the sector/canonical-archetype calibration ledger.

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
next_round = R2_holdout_or_R3_loop11
recommended_next_objective = holdout_validation or battery contract-call-off risk residual
do_not_promote_to_global = true
```

## 28. Source Notes

- stock_agent research artifacts checked only for coverage/duplicate avoidance: `reports/e2r_calibration/ingest_summary.md`, `reports/e2r_calibration/applied_scoring_diff.md`.
- stock-web price source files checked:
  - `atlas/manifest.json`
  - `atlas/schema.json`
  - `atlas/symbol_profiles/058/058470.json`
  - `atlas/symbol_profiles/095/095340.json`
  - `atlas/symbol_profiles/131/131290.json`
  - `atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/058/058470/2025.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/095/095340/2025.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv`
  - `atlas/ohlcv_tradable_by_symbol_year/131/131290/2025.csv`
