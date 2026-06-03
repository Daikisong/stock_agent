# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

- research_session: post_calibrated_sector_archetype_residual_research
- mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
- scheduled_round: R2
- scheduled_loop: 76
- large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
- canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
- fine_archetype_id: HBM_MEMORY_CUSTOMER_CAPACITY_QUALIFICATION_VS_THEME_SUPPLY_CHAIN_PROXY
- output_file: `e2r_stock_web_v12_residual_round_R2_loop_76_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md`
- production_scoring_changed: false
- shadow_weight_only: true
- handoff_prompt_embedded: true
- handoff_prompt_executed_now: false

This loop adds 4 new independent cases, 2 counterexamples, and 4 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C06_HBM_MEMORY_CUSTOMER_CAPACITY.

## 1. Current Calibrated Profile Assumption

current_default_profile_proxy = e2r_2_1_stock_web_calibrated. The already-applied axes are treated as installed and are not re-proposed globally: Stage2 actionable bonus, Yellow/Green thresholds, Green revision minimum, cross-evidence buffer, price-only blowoff guard, full 4B non-price requirement, and hard 4C thesis-break routing.

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R2 |
| scheduled_loop | 76 |
| large_sector_id | L2_AI_SEMICONDUCTOR_ELECTRONICS |
| canonical_archetype_id | C06_HBM_MEMORY_CUSTOMER_CAPACITY |
| fine_archetype_id | HBM_MEMORY_CUSTOMER_CAPACITY_QUALIFICATION_VS_THEME_SUPPLY_CHAIN_PROXY |
| round_sector_consistency | pass |
| loop_objective | residual_false_positive_mining; residual_missed_structural_mining; stage2_actionable_bonus_stress_test; green_strictness_stress_test; 4B_non_price_requirement_stress_test; canonical_archetype_compression; counterexample_mining; coverage_gap_fill |

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 outputs already contained R2 loop 72 C08, loop 73 C07, loop 74 C09, and loop 75 C10. This loop deliberately selects C06, which did not appear in those R2 v12 local outputs. Duplicate key checked: `canonical_archetype_id + symbol + trigger_type + entry_date`.

- Existing R2 symbol families avoided as primary canonical source: C08 test-socket set, C07 HBM equipment set, C09 valuation blowoff set, C10 memory-recovery equipment set.
- Reused case ids: none.
- Same-symbol reuse inside this MD: SK하이닉스 appears twice, but the trigger family differs: 2023 HBM3 customer/capacity conversion and 2024 HBM3E capacity acceleration. Both remain separate same-canonical new-trigger-family rows.

## 4. Stock-Web OHLC Input / Price Source Validation

| manifest_field | value |
|---|---|
| source_name | FinanceData/marcap |
| source_repo_url | https://github.com/FinanceData/marcap |
| price_adjustment_status | raw_unadjusted_marcap |
| min_date | 1995-05-02 |
| max_date | 2026-02-20 |
| tradable_row_count | 14354401 |
| raw_row_count | 15214118 |
| symbol_count | 5414 |
| active_like_symbol_count | 2868 |
| inactive_or_delisted_like_symbol_count | 2546 |
| markets | KONEX, KOSDAQ, KOSDAQ GLOBAL, KOSPI |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Stock-Web basis: tradable_raw / raw_unadjusted_marcap. Corporate-action candidate windows are blocked when they overlap the 180D window. The selected 2023~2024 windows do not overlap the listed corporate-action candidate dates in the profiles used here.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | 180D available | corporate_action_window_status | calibration_usable |
| --- | --- | --- | --- | --- | --- |
| R2L76_C06_000660_HBM3_20231027 | 000660 | 2023-10-27 | true | clean_180D_window | true |
| R2L76_C06_000660_HBM3E_20240213 | 000660 | 2024-02-13 | true | clean_180D_window | true |
| R2L76_C06_005930_HBM_QUALIFICATION_FALSE_POSITIVE_20240705 | 005930 | 2024-07-05 | true | clean_180D_window | true |
| R2L76_C06_067310_OSAT_CAPACITY_THEME_20230914 | 067310 | 2023-09-14 | true | clean_180D_window | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine branch | Compression rule |
|---|---|---|
| C06_HBM_MEMORY_CUSTOMER_CAPACITY | HBM_MEMORY_CUSTOMER_CAPACITY_QUALIFICATION_VS_THEME_SUPPLY_CHAIN_PROXY | Compresses direct HBM customer/capacity evidence separately from broad memory recovery and supplier-theme beta. Customer qualification and capacity conversion should raise score; unqualified broad memory beta should be capped. |

## 7. Case Selection Summary

| case_id | symbol | company | role | positive/counterexample | entry_date | entry_price | MFE_90D_pct | MAE_90D_pct | current_profile_verdict |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R2L76_C06_000660_HBM3_20231027 | 000660 | SK하이닉스 | structural_success | positive | 2023-10-27 | 119100 | 54.41 | -2.35 | current_profile_missed_structural |
| R2L76_C06_000660_HBM3E_20240213 | 000660 | SK하이닉스 | structural_success | positive | 2024-02-13 | 150000 | 62.0 | -3.4 | current_profile_too_late |
| R2L76_C06_005930_HBM_QUALIFICATION_FALSE_POSITIVE_20240705 | 005930 | 삼성전자 | false_positive_green | counterexample | 2024-07-05 | 87100 | 1.95 | -42.02 | current_profile_false_positive |
| R2L76_C06_067310_OSAT_CAPACITY_THEME_20230914 | 067310 | 하나마이크론 | failed_rerating | counterexample | 2023-09-14 | 30650 | 12.56 | -22.19 | current_profile_false_positive |

## 8. Positive vs Counterexample Balance

- positive_case_count: 2
- counterexample_count: 2
- 4B_case_count: 2
- 4C_case_count: 1 thesis-break watch-only row
- calibration_usable_case_count: 4
- representative_trigger_count: 4

The balance is intentionally not another HBM equipment rerun. It asks whether C06 memory/customer-capacity evidence can discriminate SK하이닉스-style HBM customer-capacity conversion from Samsung/Hana Micron broad-memory or OSAT-theme beta.

## 9. Evidence Source Map

| case_id | trigger_date | evidence_available_at_that_date | evidence_source | Stage2 evidence | Stage3 evidence | 4B / 4C evidence |
|---|---|---|---|---|---|---|
| R2L76_C06_000660_HBM3_20231027 | 2023-10-26 | 3Q23 loss narrowed while HBM/AI server demand and HBM3 customer visibility became investable; public earnings/disclosure evidence existed before next tradable close. | public earnings/disclosure; stock-web OHLC shard 000/000660/2023.csv and 2024.csv | public_event_or_disclosure, customer_or_order_quality, capacity_or_volume_route, early_revision_signal | confirmed_revision, margin_bridge, financial_visibility, durable_customer_confirmation | 4B=none; 4C=none |
| R2L76_C06_000660_HBM3E_20240213 | 2024-02-08 | After the February 2024 HBM/AI-memory leg, the evidence bundle was no longer only memory-cycle beta: HBM3E/customer-capacity linkage and AI server mix made capacity quality more durable than ordinary DRAM recovery. | public news/earnings context; stock-web OHLC shard 000/000660/2024.csv | public_event_or_disclosure, customer_or_order_quality, relative_strength, capacity_or_volume_route, early_revision_signal | confirmed_revision, financial_visibility, durable_customer_confirmation, low_red_team_risk | 4B=valuation_blowoff, positioning_overheat; 4C=none |
| R2L76_C06_005930_HBM_QUALIFICATION_FALSE_POSITIVE_20240705 | 2024-07-05 | Q2 2024 preliminary earnings surprise looked like memory-cycle confirmation, but HBM customer qualification and high-end AI-memory share remained contested; the trigger was more broad-memory rebound than confirmed HBM-capacity conversion. | public preliminary earnings/disclosure and contemporaneous HBM qualification news; stock-web OHLC shard 005/005930/2024.csv | public_event_or_disclosure, early_revision_signal, relative_strength | confirmed_revision, financial_visibility | 4B=margin_or_backlog_slowdown, positioning_overheat; 4C=qualification_failure, thesis_evidence_broken |
| R2L76_C06_067310_OSAT_CAPACITY_THEME_20230914 | 2023-09-14 | Back-end memory/OSAT capacity and HBM packaging theme were visible, but the row lacked direct HBM customer qualification quality. Price already reflected theme beta; subsequent MFE was small relative to MAE. | public supply-chain/theme news; stock-web OHLC shard 067/067310/2023.csv and 2024.csv | relative_strength, capacity_or_volume_route, public_event_or_disclosure | none | 4B=positioning_overheat, price_only_local_peak; 4C=none |

## 10. Price Data Source Map

| symbol | company | profile_path | price_shard_path | profile corporate action note |
|---|---|---|---|---|
| 000660 | SK하이닉스 | atlas/symbol_profiles/000/000660.json | atlas/ohlcv_tradable_by_symbol_year/000/000660/2023.csv; 2024.csv | corporate-action candidates end in 2003; selected windows clean |
| 005930 | 삼성전자 | atlas/symbol_profiles/005/005930.json | atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv | corporate-action candidates end in 2018; selected 2024 window clean |
| 067310 | 하나마이크론 | atlas/symbol_profiles/067/067310.json | atlas/ohlcv_tradable_by_symbol_year/067/067310/2023.csv; 2024.csv | corporate-action candidates 2009 and 2021; selected window clean |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | peak_date | peak_price | outcome |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R2L76_C06_000660_T1 | 000660 | Stage2-Actionable | 2023-10-26 | 2023-10-27 | 119100 | 13.01 | 54.41 | 108.65 | -2.35 | -2.35 | -2.35 | 2024-07-11 | 248500 | structural_success |
| R2L76_C06_000660_T2 | 000660 | Stage2-Actionable | 2024-02-08 | 2024-02-13 | 150000 | 22.0 | 62.0 | 65.67 | -3.4 | -3.4 | -3.4 | 2024-07-11 | 248500 | structural_success_high_later_drawdown |
| R2L76_C06_005930_T1 | 005930 | Stage2-Actionable | 2024-07-05 | 2024-07-05 | 87100 | 1.95 | 1.95 | 1.95 | -19.4 | -42.02 | -42.71 | 2024-07-11 | 88800 | failed_rerating_false_positive_green |
| R2L76_C06_067310_T1 | 067310 | Stage2-Theme | 2023-09-14 | 2023-09-14 | 30650 | 1.63 | 12.56 | 12.56 | -22.19 | -22.19 | -22.19 | 2023-11-08 | 34500 | theme_beta_failed_rerating |

## 12. Trigger-Level OHLC Backtest Tables

- MFE_N_pct = max high over the N-trading-day forward window divided by entry close minus one.
- MAE_N_pct = min low over the same forward window divided by entry close minus one.
- Peak/drawdown are computed on the observed window used in the row, with 4B interpretation kept separate from Stage2/3 scoring.

| symbol | entry_price | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | below_entry_price_flag_90D | peak_date | peak_price | drawdown_after_peak_pct |
|---|---:|---:|---:|---:|---:|---|---|---:|---:|
| 000660 | 119100 | 54.41 | -2.35 | 108.65 | -2.35 | true | 2024-07-11 | 248500 | -41.77 |
| 000660 | 150000 | 62.00 | -3.40 | 65.67 | -3.40 | true | 2024-07-11 | 248500 | -41.77 |
| 005930 | 87100 | 1.95 | -42.02 | 1.95 | -42.71 | true | 2024-07-11 | 88800 | -43.81 |
| 067310 | 30650 | 12.56 | -22.19 | 12.56 | -22.19 | true | 2023-11-08 | 34500 | -30.87 |

## 13. Current Calibrated Profile Stress Test

| case_id | current_profile_verdict | why it matters |
|---|---|---|
| R2L76_C06_000660_HBM3_20231027 | current_profile_missed_structural | Current profile can still under-recognize direct HBM customer/capacity conversion before Green confirmation, even after global Stage2 bonus. |
| R2L76_C06_000660_HBM3E_20240213 | current_profile_too_late | Green strictness remains too slow when HBM3E/customer-capacity route is no longer ordinary memory-cycle recovery. |
| R2L76_C06_005930_HBM_QUALIFICATION_FALSE_POSITIVE_20240705 | current_profile_false_positive | Broad memory earnings surprise can be over-promoted if HBM qualification/customer evidence is not separated. |
| R2L76_C06_067310_OSAT_CAPACITY_THEME_20230914 | current_profile_false_positive | OSAT/capacity theme beta without confirmed HBM customer quality produced high MAE and weak forward MFE. |

Existing calibrated axes tested: Stage2 bonus kept, Yellow/Green threshold kept globally, price-only blowoff guard strengthened, full 4B non-price requirement strengthened, hard 4C routing kept as watch-only for Samsung until thesis break is explicit.

## 14. Stage2 / Yellow / Green Comparison

| case_id | Stage2 actionable entry | Hypothetical Yellow | Hypothetical Green | green_lateness_ratio | Interpretation |
|---|---:|---|---|---:|---|
| R2L76_C06_000660_HBM3_20231027 | 119100 | 133900~140000 zone | 150000+ zone | 0.42 | Green would have captured the thesis but missed a meaningful part of the initial HBM-capacity re-rating. |
| R2L76_C06_000660_HBM3E_20240213 | 150000 | 166000~183000 zone | 190000+ zone | 0.31 | Green is not disastrously late but C06-specific bonus would improve Stage2→Yellow timing. |
| R2L76_C06_005930_HBM_QUALIFICATION_FALSE_POSITIVE_20240705 | 87100 | should remain capped | should not Green | not_applicable | Customer qualification gap should block Green. |
| R2L76_C06_067310_OSAT_CAPACITY_THEME_20230914 | 30650 | should remain capped | should not Green | not_applicable | Theme beta without customer route should not become Yellow/Green. |

## 15. 4B Local vs Full-window Timing Audit

| trigger_id | symbol | four_b_local_peak_proximity | four_b_full_window_peak_proximity | four_b_timing_verdict | four_b_evidence_type |
|---|---|---:|---:|---|---|
| R2L76_C06_000660_T1 | 000660 | n/a | n/a | not_primary_4B | none |
| R2L76_C06_000660_T2 | 000660 | n/a | n/a | not_primary_4B | valuation_blowoff; positioning_overheat later only |
| R2L76_C06_005930_T1 | 005930 | 0.93 | 0.03 | price_only_local_4B_too_early | price_only; positioning_overheat |
| R2L76_C06_067310_T1 | 067310 | 0.93 | 0.13 | price_only_local_4B_too_early | price_only; positioning_overheat |

## 16. 4C Protection Audit

Samsung's later price path behaves like a thesis-break watch row rather than an immediately hard 4C row at the July 2024 trigger date. The future hard 4C row should require explicit qualification failure/order-share loss evidence. Hana Micron is a broad theme-beta guard row, not a hard 4C.

## 17. Sector-Specific Rule Candidate

sector_specific_rule_candidate: true

Within L2, AI/HBM evidence should split into two gates:

1. `confirmed_hbm_customer_capacity_bonus`: apply only where customer quality, HBM generation/qualification, capacity allocation, and margin/revision bridge are visible together.
2. `theme_beta_without_customer_guard`: cap broad-memory or OSAT/packaging theme rows when customer qualification is not visible.

## 18. Canonical-Archetype Rule Candidate

canonical_archetype_rule_candidate: true

C06 should not inherit all C07/C10 equipment-cycle logic. It is closer to a customer-capacity conversion archetype. The C06 shadow profile should reward evidence density around HBM customer qualification/capacity and penalize memory-cycle beta without HBM customer route.

## 19. Before / After Backtest Comparison

| profile_id | profile_scope | changed_axes | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | late_green_count | score_return_alignment_verdict |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | current | none | 4 | 4 | 32.77 | -17.99 | 47.96 | -17.67 | 0.50 | 1 | 1 | mixed: positives and false positives both promoted |
| P0b e2r_2_0_baseline_reference | rollback | no Stage2 bonus, lower cross-evidence buffer | 4 | 4 | 32.77 | -17.99 | 47.96 | -17.67 | 0.25 | 2 | 2 | too conservative on SK하이닉스 C06 rows |
| P1 sector_specific_candidate_profile | sector_shadow | semiconductor customer-quality/capacity bonus + theme guard | 4 | 4 | 58.21 | -2.88 | 87.16 | -2.88 | 0.00 | 0 | 0 | best sector alignment in this loop |
| P2 canonical_archetype_candidate_profile | canonical_shadow | C06 customer/qualification gate | 4 | 4 | 58.21 | -2.88 | 87.16 | -2.88 | 0.00 | 0 | 0 | preferred candidate |
| P3 counterexample_guard_profile | canonical_guard | broad-memory theme beta cap | 4 | 4 | 58.21 | -2.88 | 87.16 | -2.88 | 0.00 | 0 | 0 | strongest false-positive control |


## 20. Score-Return Alignment Matrix

| symbol | before_score | before_stage | after_score | after_stage | MFE_90D_pct | MAE_90D_pct | alignment |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 000660 | 84 | Stage3-Yellow | 89 | Stage3-Green | 54.41 | -2.35 | positive_alignment |
| 000660 | 86 | Stage3-Yellow | 91 | Stage3-Green | 62.0 | -3.4 | positive_alignment |
| 005930 | 82 | Stage3-Yellow | 74 | Stage2-Watch | 1.95 | -42.02 | counterexample_guard_needed |
| 067310 | 76 | Stage3-Yellow | 68 | Stage2-Watch | 12.56 | -22.19 | counterexample_guard_needed |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C06_HBM_MEMORY_CUSTOMER_CAPACITY | HBM_MEMORY_CUSTOMER_CAPACITY_QUALIFICATION_VS_THEME_SUPPLY_CHAIN_PROXY | 2 | 2 | 2 | 1 | 4 | 0 | 4 | 4 | 4 | true | true | C06 still needs future explicit hard-4C customer/order-share break rows. |

## 22. Residual Contribution Summary

new_independent_case_count: 4  
reused_case_count: 0  
reused_case_ids: []  
new_symbol_count: 3  
new_canonical_archetype_count: 1  
new_fine_archetype_count: 1  
new_trigger_family_count: 4  
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min; stage3_cross_evidence_green_buffer; price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c  
residual_error_types_found: current_profile_missed_structural; current_profile_too_late; current_profile_false_positive; price_only_local_4B_too_early  
new_axis_proposed: C06_confirmed_hbm_customer_capacity_bonus; C06_theme_beta_without_customer_guard  
existing_axis_strengthened: price_only_blowoff_blocks_positive_stage; full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c  
existing_axis_weakened: null  
existing_axis_kept: stage2_actionable_evidence_bonus; stage3_yellow_total_min; stage3_green_total_min; stage3_green_revision_min; stage3_cross_evidence_green_buffer  
sector_specific_rule_candidate: true  
canonical_archetype_rule_candidate: true  
no_new_signal_reason: null  
loop_contribution_label: canonical_archetype_rule_candidate  
do_not_propose_new_weight_delta: false

## 23. Validation Scope / Non-Validation Scope

Validated:

- Stock-Web manifest max_date and calibration shard roots.
- Entry rows and representative forward-window price path from stock-web tradable shards.
- 180D windows are available and not overlapped by the profile corporate-action candidate dates.
- Dedupe uses representative trigger per same_entry_group_id.

Not validated in this loop:

- Production scoring code.
- Live candidate discovery.
- Full 2Y forward path for all rows.
- Hard 4C production routing, because explicit customer/order-share break evidence should be added in a future C06 red-team row.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C06_confirmed_hbm_customer_capacity_bonus,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"Reward HBM evidence only when customer/qualification/capacity route is visible, not merely memory-cycle recovery.","SK하이닉스 positive rows remain high-MFE while Samsung/Hana theme rows are demoted.",R2L76_C06_000660_T1|R2L76_C06_000660_T2|R2L76_C06_005930_T1|R2L76_C06_067310_T1,4,4,2,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C06_theme_beta_without_customer_guard,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"Penalize broad-memory/HBM theme rows where customer qualification is unconfirmed.","Reduces false positive Stage3-Yellow/Green on Samsung and Hana Micron rows.",R2L76_C06_005930_T1|R2L76_C06_067310_T1,4,4,2,medium,counterexample_guard_shadow_only,"not production; post-calibrated residual"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R2L76_C06_000660_HBM3_20231027", "symbol": "000660", "company_name": "SK하이닉스", "round": "R2", "loop": "76", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_MEMORY_CUSTOMER_CAPACITY_QUALIFICATION_VS_THEME_SUPPLY_CHAIN_PROXY", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R2L76_C06_000660_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_missed_structural", "price_source": "Songdaiki/stock-web", "notes": "3Q23 loss narrowed while HBM/AI server demand and HBM3 customer visibility became investable; public earnings/disclosure evidence existed before next tradable close."}
{"row_type": "case", "case_id": "R2L76_C06_000660_HBM3E_20240213", "symbol": "000660", "company_name": "SK하이닉스", "round": "R2", "loop": "76", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_MEMORY_CUSTOMER_CAPACITY_QUALIFICATION_VS_THEME_SUPPLY_CHAIN_PROXY", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R2L76_C06_000660_T2", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "After the February 2024 HBM/AI-memory leg, the evidence bundle was no longer only memory-cycle beta: HBM3E/customer-capacity linkage and AI server mix made capacity quality more durable than ordinary DRAM recovery."}
{"row_type": "case", "case_id": "R2L76_C06_005930_HBM_QUALIFICATION_FALSE_POSITIVE_20240705", "symbol": "005930", "company_name": "삼성전자", "round": "R2", "loop": "76", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_MEMORY_CUSTOMER_CAPACITY_QUALIFICATION_VS_THEME_SUPPLY_CHAIN_PROXY", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R2L76_C06_005930_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "misaligned_or_false_positive", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Q2 2024 preliminary earnings surprise looked like memory-cycle confirmation, but HBM customer qualification and high-end AI-memory share remained contested; the trigger was more broad-memory rebound than confirmed HBM-capacity conversion."}
{"row_type": "case", "case_id": "R2L76_C06_067310_OSAT_CAPACITY_THEME_20230914", "symbol": "067310", "company_name": "하나마이크론", "round": "R2", "loop": "76", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_MEMORY_CUSTOMER_CAPACITY_QUALIFICATION_VS_THEME_SUPPLY_CHAIN_PROXY", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R2L76_C06_067310_T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "misaligned_or_false_positive", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Back-end memory/OSAT capacity and HBM packaging theme were visible, but the row lacked direct HBM customer qualification quality. Price already reflected theme beta; subsequent MFE was small relative to MAE."}
{"row_type": "trigger", "trigger_id": "R2L76_C06_000660_T1", "case_id": "R2L76_C06_000660_HBM3_20231027", "symbol": "000660", "company_name": "SK하이닉스", "round": "R2", "loop": "76", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_MEMORY_CUSTOMER_CAPACITY_QUALIFICATION_VS_THEME_SUPPLY_CHAIN_PROXY", "sector": "AI semiconductor/electronics", "primary_archetype": "HBM memory customer-capacity qualification vs theme beta", "loop_objective": "residual_false_positive_mining|residual_missed_structural_mining|stage2_actionable_bonus_stress_test|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-10-26", "entry_date": "2023-10-27", "entry_price": 119100, "evidence_available_at_that_date": "3Q23 loss narrowed while HBM/AI server demand and HBM3 customer visibility became investable; public earnings/disclosure evidence existed before next tradable close.", "evidence_source": "public earnings/disclosure; stock-web OHLC shard 000/000660/2023.csv and 2024.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "margin_bridge", "financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000660/2023.csv", "profile_path": "atlas/symbol_profiles/000/000660.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 13.01, "MFE_90D_pct": 54.41, "MFE_180D_pct": 108.65, "MFE_1Y_pct": 108.65, "MFE_2Y_pct": null, "MAE_30D_pct": -2.35, "MAE_90D_pct": -2.35, "MAE_180D_pct": -2.35, "MAE_1Y_pct": -2.35, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-11", "peak_price": 248500, "drawdown_after_peak_pct": -41.77, "green_lateness_ratio": 0.42, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_primary_4B", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_missed_structural", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R2L76_C06_000660_HBM3_20231027_EG1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R2L76_C06_000660_T2", "case_id": "R2L76_C06_000660_HBM3E_20240213", "symbol": "000660", "company_name": "SK하이닉스", "round": "R2", "loop": "76", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_MEMORY_CUSTOMER_CAPACITY_QUALIFICATION_VS_THEME_SUPPLY_CHAIN_PROXY", "sector": "AI semiconductor/electronics", "primary_archetype": "HBM memory customer-capacity qualification vs theme beta", "loop_objective": "residual_false_positive_mining|residual_missed_structural_mining|stage2_actionable_bonus_stress_test|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-02-08", "entry_date": "2024-02-13", "entry_price": 150000, "evidence_available_at_that_date": "After the February 2024 HBM/AI-memory leg, the evidence bundle was no longer only memory-cycle beta: HBM3E/customer-capacity linkage and AI server mix made capacity quality more durable than ordinary DRAM recovery.", "evidence_source": "public news/earnings context; stock-web OHLC shard 000/000660/2024.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "relative_strength", "capacity_or_volume_route", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "durable_customer_confirmation", "low_red_team_risk"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv", "profile_path": "atlas/symbol_profiles/000/000660.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 22.0, "MFE_90D_pct": 62.0, "MFE_180D_pct": 65.67, "MFE_1Y_pct": 65.67, "MFE_2Y_pct": null, "MAE_30D_pct": -3.4, "MAE_90D_pct": -3.4, "MAE_180D_pct": -3.4, "MAE_1Y_pct": -3.4, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-11", "peak_price": 248500, "drawdown_after_peak_pct": -41.77, "green_lateness_ratio": 0.31, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_primary_4B", "four_b_evidence_type": ["valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success_high_later_drawdown", "current_profile_verdict": "current_profile_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R2L76_C06_000660_HBM3E_20240213_EG1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R2L76_C06_005930_T1", "case_id": "R2L76_C06_005930_HBM_QUALIFICATION_FALSE_POSITIVE_20240705", "symbol": "005930", "company_name": "삼성전자", "round": "R2", "loop": "76", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_MEMORY_CUSTOMER_CAPACITY_QUALIFICATION_VS_THEME_SUPPLY_CHAIN_PROXY", "sector": "AI semiconductor/electronics", "primary_archetype": "HBM memory customer-capacity qualification vs theme beta", "loop_objective": "residual_false_positive_mining|residual_missed_structural_mining|stage2_actionable_bonus_stress_test|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-05", "entry_date": "2024-07-05", "entry_price": 87100, "evidence_available_at_that_date": "Q2 2024 preliminary earnings surprise looked like memory-cycle confirmation, but HBM customer qualification and high-end AI-memory share remained contested; the trigger was more broad-memory rebound than confirmed HBM-capacity conversion.", "evidence_source": "public preliminary earnings/disclosure and contemporaneous HBM qualification news; stock-web OHLC shard 005/005930/2024.csv", "stage2_evidence_fields": ["public_event_or_disclosure", "early_revision_signal", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "positioning_overheat"], "stage4c_evidence_fields": ["qualification_failure", "thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv", "profile_path": "atlas/symbol_profiles/005/005930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.95, "MFE_90D_pct": 1.95, "MFE_180D_pct": 1.95, "MFE_1Y_pct": 1.95, "MFE_2Y_pct": null, "MAE_30D_pct": -19.4, "MAE_90D_pct": -42.02, "MAE_180D_pct": -42.71, "MAE_1Y_pct": -42.71, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-11", "peak_price": 88800, "drawdown_after_peak_pct": -43.81, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.93, "four_b_full_window_peak_proximity": 0.03, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating_false_positive_green", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R2L76_C06_005930_HBM_QUALIFICATION_FALSE_POSITIVE_20240705_EG1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R2L76_C06_067310_T1", "case_id": "R2L76_C06_067310_OSAT_CAPACITY_THEME_20230914", "symbol": "067310", "company_name": "하나마이크론", "round": "R2", "loop": "76", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_MEMORY_CUSTOMER_CAPACITY_QUALIFICATION_VS_THEME_SUPPLY_CHAIN_PROXY", "sector": "AI semiconductor/electronics", "primary_archetype": "HBM memory customer-capacity qualification vs theme beta", "loop_objective": "residual_false_positive_mining|residual_missed_structural_mining|stage2_actionable_bonus_stress_test|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression|counterexample_mining|coverage_gap_fill", "trigger_type": "Stage2-Theme", "trigger_date": "2023-09-14", "entry_date": "2023-09-14", "entry_price": 30650, "evidence_available_at_that_date": "Back-end memory/OSAT capacity and HBM packaging theme were visible, but the row lacked direct HBM customer qualification quality. Price already reflected theme beta; subsequent MFE was small relative to MAE.", "evidence_source": "public supply-chain/theme news; stock-web OHLC shard 067/067310/2023.csv and 2024.csv", "stage2_evidence_fields": ["relative_strength", "capacity_or_volume_route", "public_event_or_disclosure"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/067/067310/2023.csv", "profile_path": "atlas/symbol_profiles/067/067310.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 1.63, "MFE_90D_pct": 12.56, "MFE_180D_pct": 12.56, "MFE_1Y_pct": 12.56, "MFE_2Y_pct": null, "MAE_30D_pct": -22.19, "MAE_90D_pct": -22.19, "MAE_180D_pct": -22.19, "MAE_1Y_pct": -22.19, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-11-08", "peak_price": 34500, "drawdown_after_peak_pct": -30.87, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.93, "four_b_full_window_peak_proximity": 0.13, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "theme_beta_failed_rerating", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R2L76_C06_067310_OSAT_CAPACITY_THEME_20230914_EG1", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L76_C06_000660_HBM3_20231027", "trigger_id": "R2L76_C06_000660_T1", "symbol": "000660", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "raw_component_scores_before": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 11, "revision_score": 20, "relative_strength_score": 12, "customer_quality_score": 10, "policy_or_regulatory_score": 2, "valuation_repricing_score": 8, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 84, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 8, "backlog_visibility_score": 8, "margin_bridge_score": 11, "revision_score": 21, "relative_strength_score": 12, "customer_quality_score": 12, "policy_or_regulatory_score": 2, "valuation_repricing_score": 8, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 2}, "weighted_score_after": 89, "stage_label_after": "Stage3-Green", "changed_components": ["customer_quality_score", "capacity_or_shipment_score", "revision_score"], "component_delta_explanation": "C06 shadow profile rewards confirmed HBM customer/capacity linkage and penalizes broad-memory theme beta without qualification/customer confirmation.", "MFE_90D_pct": 54.41, "MAE_90D_pct": -2.35, "score_return_alignment_label": "positive_alignment", "current_profile_verdict": "current_profile_missed_structural"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L76_C06_000660_HBM3E_20240213", "trigger_id": "R2L76_C06_000660_T2", "symbol": "000660", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "raw_component_scores_before": {"contract_score": 7, "backlog_visibility_score": 9, "margin_bridge_score": 10, "revision_score": 22, "relative_strength_score": 13, "customer_quality_score": 11, "policy_or_regulatory_score": 2, "valuation_repricing_score": 8, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 86, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 7, "backlog_visibility_score": 10, "margin_bridge_score": 10, "revision_score": 22, "relative_strength_score": 13, "customer_quality_score": 13, "policy_or_regulatory_score": 2, "valuation_repricing_score": 8, "execution_risk_score": 3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "capacity_or_shipment_score": 2}, "weighted_score_after": 91, "stage_label_after": "Stage3-Green", "changed_components": ["customer_quality_score", "capacity_or_shipment_score", "backlog_visibility_score"], "component_delta_explanation": "C06 shadow profile rewards confirmed HBM customer/capacity linkage and penalizes broad-memory theme beta without qualification/customer confirmation.", "MFE_90D_pct": 62.0, "MAE_90D_pct": -3.4, "score_return_alignment_label": "positive_alignment", "current_profile_verdict": "current_profile_too_late"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L76_C06_005930_HBM_QUALIFICATION_FALSE_POSITIVE_20240705", "trigger_id": "R2L76_C06_005930_T1", "symbol": "005930", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 3, "margin_bridge_score": 12, "revision_score": 23, "relative_strength_score": 12, "customer_quality_score": 3, "policy_or_regulatory_score": 1, "valuation_repricing_score": 10, "execution_risk_score": 7, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 3, "margin_bridge_score": 12, "revision_score": 23, "relative_strength_score": 12, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 10, "execution_risk_score": 10, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "qualification_gap_risk_score": 5}, "weighted_score_after": 74, "stage_label_after": "Stage2-Watch", "changed_components": ["customer_quality_score", "execution_risk_score", "qualification_gap_risk_score"], "component_delta_explanation": "C06 shadow profile rewards confirmed HBM customer/capacity linkage and penalizes broad-memory theme beta without qualification/customer confirmation.", "MFE_90D_pct": 1.95, "MAE_90D_pct": -42.02, "score_return_alignment_label": "counterexample_guard_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L76_C06_067310_OSAT_CAPACITY_THEME_20230914", "trigger_id": "R2L76_C06_067310_T1", "symbol": "067310", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "raw_component_scores_before": {"contract_score": 2, "backlog_visibility_score": 4, "margin_bridge_score": 4, "revision_score": 10, "relative_strength_score": 19, "customer_quality_score": 2, "policy_or_regulatory_score": 1, "valuation_repricing_score": 12, "execution_risk_score": 8, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 2, "backlog_visibility_score": 4, "margin_bridge_score": 4, "revision_score": 10, "relative_strength_score": 19, "customer_quality_score": 0, "policy_or_regulatory_score": 1, "valuation_repricing_score": 12, "execution_risk_score": 12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "theme_beta_without_customer_gate": 6}, "weighted_score_after": 68, "stage_label_after": "Stage2-Watch", "changed_components": ["customer_quality_score", "execution_risk_score", "theme_beta_without_customer_gate"], "component_delta_explanation": "C06 shadow profile rewards confirmed HBM customer/capacity linkage and penalizes broad-memory theme beta without qualification/customer confirmation.", "MFE_90D_pct": 12.56, "MAE_90D_pct": -22.19, "score_return_alignment_label": "counterexample_guard_needed", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "residual_contribution", "round": "R2", "loop": "76", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 3, "same_archetype_new_symbol_count": 3, "same_archetype_new_trigger_family_count": 4, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "stage3_green_revision_min", "stage3_cross_evidence_green_buffer", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["current_profile_missed_structural", "current_profile_too_late", "current_profile_false_positive", "price_only_local_4B_too_early"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
{"row_type": "narrative_only", "case_id": "R2L76_C06_future_4C_needed", "symbol": null, "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "reason": "hard 4C can be strengthened later with explicit HBM customer qualification failure/order cut rows; this loop treats Samsung as thesis-break watch rather than production 4C.", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}
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

completed_round = R2  
completed_loop = 76  
next_round = R3  
next_loop = 76  
round_schedule_status = valid  
round_sector_consistency = pass

## 28. Source Notes

- Price atlas: Songdaiki/stock-web manifest, schema, symbol profile files, and tradable OHLC shards.
- Primary price rows used: `000/000660/2023.csv`, `000/000660/2024.csv`, `005/005930/2024.csv`, `067/067310/2023.csv`, `067/067310/2024.csv`.
- Evidence labels are historical research proxies. They are not investment recommendations and do not alter production scoring.

