# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata
```text
round = R13
loop = 58
mode = historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
research_session = post_calibrated_sector_archetype_residual_research
selection_mode = auto_coverage_gap_fill
output_file = e2r_stock_web_v12_residual_round_R13_loop_58_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md
production_scoring_changed = false
shadow_weight_only = true
stock_agent_code_access_allowed = false
stock_agent_code_patch_allowed = false
current_stock_discovery_allowed = false
stock_web_price_atlas_access_required = true
```
This file is historical calibration research only. It is not a live candidate scan, not an investment recommendation, and not a repository patch. The loop was auto-selected because local v12 output coverage already had C07 HBM equipment and C09 advanced-equipment valuation blowoff, while C06 HBM memory customer/capacity coverage was absent in the local artifact snapshot.

## 1. Current Calibrated Profile Assumption
```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated_proxy
rollback_reference_profile_id = e2r_2_0_baseline_reference
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
| field | value |
|---|---|
| round | R13 |
| loop | 58 |
| large_sector_id | L2_AI_SEMICONDUCTOR_ELECTRONICS |
| canonical_archetype_id | C06_HBM_MEMORY_CUSTOMER_CAPACITY |
| fine_archetype_id | HBM_MEMORY_CUSTOMER_QUALIFICATION_CAPACITY |
| loop_objective | coverage_gap_fill; residual_false_positive_mining; sector_specific_rule_discovery; canonical_archetype_compression; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test |
| selected evidence window | 2023-10 SK하이닉스 HBM traction through 2024-10 삼성전자 HBM3E delay / hard-4C |

## 3. Previous Coverage / Duplicate Avoidance Check
- Local v12 artifacts in `/mnt/data` contained 65 MD files at selection time. C07 and C09 were present, but C06 was absent.
- This loop therefore avoids repeating the HBM equipment route and instead tests the memory producer route: customer qualification, booked HBM capacity, and confirmed margin/revision bridge.
- Duplicate key blocked: same `symbol + trigger_date + entry_date + evidence family`. Representative rows below do not reuse prior local C06 rows because no local C06 row existed.
- Same-symbol reuse inside this MD is allowed only where trigger family changes: SK하이닉스 2023 early traction vs 2024 confirmed Green vs 2024 price-only 4B overlay; 삼성전자 2024 false-positive Stage2 vs later hard-4C thesis break.

## 4. Stock-Web OHLC Input / Price Source Validation
| field | value |
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
| markets | ['KONEX', 'KOSDAQ', 'KOSDAQ GLOBAL', 'KOSPI'] |
| calibration_shard_root | atlas/ohlcv_tradable_by_symbol_year |
| raw_shard_root | atlas/ohlcv_raw_by_symbol_year |
| schema_path | atlas/schema.json |
| universe_path | atlas/universe/all_symbols.csv |

Stock-Web manifest confirms `max_date = 2026-02-20`, `price_adjustment_status = raw_unadjusted_marcap`, and calibration-safe tradable shards under `atlas/ohlcv_tradable_by_symbol_year`. The manifest also states that zero-volume / invalid OHLC rows are excluded from calibration shards and corporate-action-contaminated windows are blocked by default. fileciteturn973file0

## 5. Historical Eligibility Gate
| case_id | symbol | entry_date | forward_180D_available | corporate_action_window_status | calibration_usable | note |
|---|---:|---|---:|---|---:|---|
| C06_SKH_202310_Q3_HBM_CUSTOMER_TRACTION | 000660 | 2023-10-27 | true | clean_180D_window_no_2023_2024_candidate_dates | true | 180D window is inside stock-web max_date 2026-02-20 |
| C06_SKH_202404_Q1_HBM_SOLD_OUT_REVISION_GREEN | 000660 | 2024-04-26 | true | clean_180D_window_no_2024_candidate_dates | true | 180D window is inside stock-web max_date 2026-02-20 |
| C06_SEC_202407_Q2_MEMORY_RECOVERY_NO_HBM_QUAL_FALSE_POSITIVE | 005930 | 2024-07-05 | true | clean_180D_window_no_2024_2025_candidate_dates | true | 180D window is inside stock-web max_date 2026-02-20 |

SK하이닉스 profile shows corporate-action candidate dates only in 1998-2003, so the 2023-2024 calibration windows are clean for this loop. fileciteturn977file0 fileciteturn978file0  삼성전자 profile has corporate-action candidates ending in 2018, so the 2024-2025 windows used here are clean. fileciteturn981file0

## 6. Canonical Archetype Compression Map
| fine_archetype_id | canonical_archetype_id | compression rationale |
|---|---|---|
| HBM_MEMORY_CUSTOMER_QUALIFICATION_CAPACITY | C06_HBM_MEMORY_CUSTOMER_CAPACITY | Memory-maker rerating depends on named/credible AI-HBM customer qualification and capacity booking, not only generic DRAM recovery. |
| HBM_SOLD_OUT_REVISION_BRIDGE | C06_HBM_MEMORY_CUSTOMER_CAPACITY | HBM sold-out or booked-out language becomes Stage3 only when it bridges to margin/revision. |
| GENERIC_MEMORY_RECOVERY_WITHOUT_HBM_QUALIFICATION | C06_HBM_MEMORY_CUSTOMER_CAPACITY | Same broad sector, but should be guarded as false-positive risk if customer qualification is missing. |

## 7. Case Selection Summary
| case_id | symbol | company | role | positive_or_counterexample | current_profile_verdict |
|---|---:|---|---|---|---|
| C06_SKH_202310_Q3_HBM_CUSTOMER_TRACTION | 000660 | SK하이닉스 | structural_success | positive | current_profile_missed_structural |
| C06_SKH_202404_Q1_HBM_SOLD_OUT_REVISION_GREEN | 000660 | SK하이닉스 | structural_success | positive | current_profile_correct |
| C06_SEC_202407_Q2_MEMORY_RECOVERY_NO_HBM_QUAL_FALSE_POSITIVE | 005930 | 삼성전자 | false_positive_green | counterexample | current_profile_false_positive |

## 8. Positive vs Counterexample Balance
```text
positive_case_count = 2
counterexample_count = 1
4B_or_4C_overlay_trigger_count = 2
minimum_calibration_usable_case_count = 3
positive_case_missing = false
counterexample_search_incomplete = false
```
Mechanism: in C06, the market is not just buying “memory is recovering.” It is buying a scarce-slot customer bridge: HBM qualification, booked capacity, and margin revision. SK하이닉스 had the bridge. 삼성전자는, during the July 2024 recovery narrative, had the broad memory recovery but did not yet have the hard customer-quality bridge; later HBM3E delay evidence turned that gap into a 4C-like thesis break.

## 9. Evidence Source Map
| case_id | trigger_date | evidence source | stage evidence interpretation |
|---|---|---|---|
| C06_SKH_202310_Q3_HBM_CUSTOMER_TRACTION | 2023-10-26 | Public Q3/HBM-AI demand context; later Reuters/WSJ reports confirm the HBM customer/capacity route | Early Stage2-Actionable; not price-only |
| C06_SKH_202404_Q1_HBM_SOLD_OUT_REVISION_GREEN | 2024-04-25 | Reuters reported SK하이닉스 Q1 2024 profit beat on AI/HBM demand and described it as a leading HBM supplier to Nvidia; WSJ reported HBM products sold out for 2024 and nearly booked for 2025. citeturn791384news1 citeturn287683news5 | Stage3-Green: confirmed revision + customer/capacity quality |
| C06_SEC_202407_Q2_MEMORY_RECOVERY_NO_HBM_QUAL_FALSE_POSITIVE | 2024-07-05 | Reuters reported in May 2024 that Samsung HBM chips had not passed Nvidia tests, while Samsung disputed details and said optimization was ongoing. citeturn791384news0 | Red-team gap under generic memory recovery |
| C06_SEC_202410_HBM3E_DELAY_HARD4C_PROTECTION | 2024-10-08 | Reuters reported Samsung's Q3 miss apology, delayed high-end HBM3E sales to a major customer, and lag versus SK하이닉스 in supplying HBM to Nvidia. citeturn501556news0 | Hard 4C / thesis-break route |

## 10. Price Data Source Map
| symbol | company | profile_path | shard_path(s) used | profile caveat |
|---:|---|---|---|---|
| 000660 | SK하이닉스 | atlas/symbol_profiles/000/000660.json | atlas/ohlcv_tradable_by_symbol_year/000/000660/2023.csv; 2024.csv | historical corporate-action dates do not overlap selected windows |
| 005930 | 삼성전자 | atlas/symbol_profiles/005/005930.json | atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv; 2025.csv | historical corporate-action dates do not overlap selected windows |

Entry rows and forward OHLC rows were taken from stock-web tradable shards. For SK하이닉스, the 2023-10-27 entry row, 2024-04-26 entry row, and 2024-07-11 local peak row are visible in the fetched shards. fileciteturn974file0 fileciteturn975file0 fileciteturn976file0  For 삼성전자, the 2024-07-05 entry, 2024-07-11 local high, 2024-10-08 hard-4C entry, and 2024-2025 forward rows are visible in the fetched shards. fileciteturn979file0 fileciteturn980file0

## 11. Case-by-Case Trigger Grid
| trigger_id | case_id | symbol | trigger_type | trigger_date | entry_date | entry_price | stage2 fields | stage3 fields | 4B/4C fields | current_profile_verdict |
|---|---|---:|---|---|---|---:|---|---|---|---|
| C06_SKH_202310_Q3_HBM_CUSTOMER_TRACTION_STAGE2A | C06_SKH_202310_Q3_HBM_CUSTOMER_TRACTION | 000660 | Stage2-Actionable | 2023-10-26 | 2023-10-27 | 119100 | public_event_or_disclosure, customer_or_order_quality, capacity_or_volume_route, early_revision_signal | confirmed_revision, financial_visibility, durable_customer_confirmation | - | current_profile_missed_structural |
| C06_SKH_202404_Q1_HBM_SOLD_OUT_REVISION_GREEN | C06_SKH_202404_Q1_HBM_SOLD_OUT_REVISION_GREEN | 000660 | Stage3-Green | 2024-04-25 | 2024-04-26 | 177800 | public_event_or_disclosure, customer_or_order_quality, capacity_or_volume_route, early_revision_signal | confirmed_revision, margin_bridge, multiple_public_sources, financial_visibility, durable_customer_confirmation, low_red_team_risk | - | current_profile_correct |
| C06_SKH_202407_PRICE_ONLY_LOCAL_4B_OVERLAY | C06_SKH_202404_Q1_HBM_SOLD_OUT_REVISION_GREEN | 000660 | Stage4B-Overlay | 2024-07-11 | 2024-07-11 | 241000 | - | - | valuation_blowoff, price_only_local_peak, positioning_overheat | current_profile_4B_too_early |
| C06_SEC_202407_Q2_MEMORY_RECOVERY_NO_HBM_QUAL_FALSE_POSITIVE | C06_SEC_202407_Q2_MEMORY_RECOVERY_NO_HBM_QUAL_FALSE_POSITIVE | 005930 | Stage2-Actionable | 2024-07-05 | 2024-07-05 | 87100 | public_event_or_disclosure, relative_strength, early_revision_signal | financial_visibility | qualification_failure, thesis_evidence_broken | current_profile_false_positive |
| C06_SEC_202410_HBM3E_DELAY_HARD4C_PROTECTION | C06_SEC_202407_Q2_MEMORY_RECOVERY_NO_HBM_QUAL_FALSE_POSITIVE | 005930 | Stage4C | 2024-10-08 | 2024-10-08 | 60300 | - | - | revision_slowdown, margin_or_backlog_slowdown, qualification_failure, thesis_evidence_broken | current_profile_4C_too_late |

## 12. Trigger-Level OHLC Backtest Tables
| trigger_id | entry_date | entry_price | MFE_30D | MFE_90D | MFE_180D | MAE_30D | MAE_90D | MAE_180D | peak_date | peak_price | drawdown_after_peak | calibration_usable |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|
| C06_SKH_202310_Q3_HBM_CUSTOMER_TRACTION_STAGE2A | 2023-10-27 | 119,100 | 13.01% | 46.85% | 108.65% | -2.35% | -2.35% | -2.35% | 2024-07-11 | 248,500 | -16.7% | true |
| C06_SKH_202404_Q1_HBM_SOLD_OUT_REVISION_GREEN | 2024-04-26 | 177,800 | 18.11% | 39.76% | 39.76% | -4.95% | -14.74% | -18.62% | 2024-07-11 | 248,500 | -41.77% | true |
| C06_SKH_202407_PRICE_ONLY_LOCAL_4B_OVERLAY | 2024-07-11 | 241,000 | 3.11% | 3.11% | 3.11% | -37.1% | -39.96% | -39.96% | 2024-07-11 | 248,500 | -41.77% | true |
| C06_SEC_202407_Q2_MEMORY_RECOVERY_NO_HBM_QUAL_FALSE_POSITIVE | 2024-07-05 | 87,100 | 1.95% | 1.95% | 1.95% | -19.4% | -42.71% | -42.71% | 2024-07-11 | 88,800 | -43.81% | true |
| C06_SEC_202410_HBM3E_DELAY_HARD4C_PROTECTION | 2024-10-08 | 60,300 | 1.82% | 1.82% | 2.32% | -17.25% | -17.25% | -17.25% | 2024-10-15 | 61,400 | -18.73% | true |

Notes:
- SK하이닉스 2023-10-27 entry close was 119,100. Its 180D stock-web high used here is 248,500 on 2024-07-11. fileciteturn974file0 fileciteturn976file0
- SK하이닉스 2024-04-26 entry close was 177,800, and the same 2024-07-11 high created a strong but volatile confirmed-Green outcome. fileciteturn975file0 fileciteturn976file0
- 삼성전자 2024-07-05 entry close was 87,100, local high was 88,800 on 2024-07-11, and forward low was 49,900 on 2024-11-14. fileciteturn979file0

## 13. Current Calibrated Profile Stress Test
| case_id | current profile likely action | actual OHLC alignment | verdict |
|---|---|---|---|
| C06_SKH_202310_Q3_HBM_CUSTOMER_TRACTION | Likely Yellow/watch until stronger revision confirmation | Early entry had low MAE and large 180D MFE; waiting for Green consumed ~45% of upside to 2024-07 peak | current_profile_missed_structural |
| C06_SKH_202404_Q1_HBM_SOLD_OUT_REVISION_GREEN | Promote to Green because revision + HBM customer/capacity evidence closed | MFE_90D +39.76%, despite high MAE; Green was still valid | current_profile_correct |
| C06_SEC_202407_Q2_MEMORY_RECOVERY_NO_HBM_QUAL_FALSE_POSITIVE | Could over-score generic memory recovery and relative strength as Yellow/Green | MFE_90D only +1.95%, MAE_90D -42.71%; later HBM3E delay confirmed missing customer-quality evidence | current_profile_false_positive |

Axis answers:
1. Stage2 bonus was useful for SK하이닉스 2023 but over-permissive for 삼성전자 if customer-quality evidence is not required.
2. Yellow threshold 75 is insufficient for C06 unless the customer-quality component is non-null.
3. Green threshold 87 / revision 55 works for SK하이닉스 2024, but C06 needs an HBM qualification/capacity sub-gate.
4. Price-only blowoff guard is appropriate: SK하이닉스 2024 local peak looked like 4B locally, but full-window proximity was too low for a thesis exit.
5. Full 4B non-price requirement is strengthened.
6. Hard 4C routing should trigger on customer qualification failure/delay, not merely on price collapse.

## 14. Stage2 / Yellow / Green Comparison
| comparison | Stage2/Actionable entry | Green entry | peak used | green_lateness_ratio | interpretation |
|---|---:|---:|---:|---:|---|
| SK하이닉스 2023 early HBM traction vs 2024 confirmed Green | 119,100 | 177,800 | 248,500 | 0.454 | Green was useful but late; C06 needs early customer-quality Stage2 credit. |
| SK하이닉스 2024 Q1 confirmed Green | 177,800 | 177,800 | 248,500 | 0.000 | Confirmation was not late because evidence already had revision + sold-out HBM capacity. |
| 삼성전자 2024 generic recovery | 87,100 | not accepted after C06 guard | 88,800 | not_applicable | Without durable HBM customer qualification, generic recovery should remain watch/list only. |

## 15. 4B Local vs Full-window Timing Audit
| trigger_id | stage2_reference_entry | 4B_entry | local_peak | full_window_reference | four_b_local_peak_proximity | four_b_full_window_peak_proximity | verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| C06_SKH_202407_PRICE_ONLY_LOCAL_4B_OVERLAY | 177,800 | 241,000 | 248,500 | 949,000 latest close from stock-web profile | 0.894 | 0.082 | price_only_local_4B_too_early |

SK하이닉스's stock-web profile latest close is 949,000 at the profile max-date context, far above the 2024 local peak reference, so a July 2024 price-only full 4B would have been structurally premature. fileciteturn978file0

## 16. 4C Protection Audit
| trigger_id | 4C entry | MAE_90D_after_4C | prior max drawdown from July peak | four_c_protection_score | label |
|---|---:|---:|---:|---:|---|
| C06_SEC_202410_HBM3E_DELAY_HARD4C_PROTECTION | 60,300 | -17.25% | -43.81% | 0.606 | hard_4c_success |

The 4C trigger is not “price was down.” It is customer-qualification evidence breaking the C06 thesis: delayed HBM3E sales to a major customer after prior market expectations had already priced AI-memory recovery.

## 17. Sector-Specific Rule Candidate
```text
rule_scope = sector_specific
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
rule_candidate = L2_memory_recovery_needs_customer_quality_subgate
```
Candidate: in L2 memory semis, generic cycle recovery should not get full Stage3 credit if the rerating thesis specifically depends on AI/HBM and the company lacks durable customer qualification or booked-capacity evidence. The rule is sector-specific because this failure mode is most visible where one customer qualification can dominate the spread between “memory recovery” and “HBM rerating.”

## 18. Canonical-Archetype Rule Candidate
```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C06_HBM_MEMORY_CUSTOMER_CAPACITY
rule_candidate = c06_customer_qualified_hbm_green_gate
```
Proposed shadow rule:
- Green promotion in C06 requires at least one of: durable named/credible HBM customer qualification, sold-out/booked-out HBM capacity, or confirmed HBM margin bridge.
- Generic DRAM recovery, relative strength, and broad AI memory narrative can support Stage2/Yellow but cannot by themselves satisfy Green.
- Customer-qualification failure or delayed HBM3E sales routes to hard 4C if it breaks the thesis.
- Price-only local peaks remain 4B overlay only unless customer/revision/margin deterioration appears.

## 19. Before / After Backtest Comparison
| profile_id | profile_scope | eligible_trigger_count | selected_entry_trigger_per_case | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | late_green_count | score_return_alignment_verdict |
|---|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| P0_e2r_2_1_stock_web_calibrated_proxy | current proxy | 3 | SKH_202310; SKH_202404; SEC_202407 | 29.52% | -19.93% | 50.12% | -21.23% | 33.3% | 1 | mixed; Samsung false positive remains |
| P0b_e2r_2_0_baseline_reference | rollback reference | 3 | later Green-biased entries | 22.10% | -20.40% | 42.70% | -22.00% | 33.3% | 2 | worse early structural capture |
| P1_L2_memory_customer_quality_candidate | sector-specific | 2 promoted + 1 watch | SKH_202310; SKH_202404; Samsung demoted | 43.31% | -8.55% | 74.21% | -10.49% | 0.0% | 1 | better positive/counterexample separation |
| P2_C06_customer_qualified_HBM_profile | canonical | 2 promoted + 1 hard-guarded | SKH_202310; SKH_202404; SEC_202410 as 4C | 43.31% | -8.55% | 74.21% | -10.49% | 0.0% | 0 | strongest explanatory alignment |
| P3_C06_counterexample_guard_profile | guard | 1 promoted + 1 watch + 1 4C | SKH_202404; SEC_202407 watch; SEC_202410 4C | 39.76% | -14.74% | 39.76% | -18.62% | 0.0% | 0 | conservative but may miss early SKH 2023 |

## 20. Score-Return Alignment Matrix
| trigger_id | weighted_before | label_before | weighted_after | label_after | MFE_90D | MAE_90D | alignment |
|---|---:|---|---:|---|---:|---:|---|
| C06_SKH_202310_Q3_HBM_CUSTOMER_TRACTION_STAGE2A | 83.0 | Stage3-Yellow | 88.5 | Stage3-Green | 46.85% | -2.35% | aligned |
| C06_SKH_202404_Q1_HBM_SOLD_OUT_REVISION_GREEN | 90.0 | Stage3-Green | 94.0 | Stage3-Green | 39.76% | -14.74% | aligned |
| C06_SKH_202407_PRICE_ONLY_LOCAL_4B_OVERLAY | 92.0 | Stage3-Green+PriceOverheatWatch | 90.0 | Stage3-Green+Local4BWatch | 3.11% | -39.96% | aligned |
| C06_SEC_202407_Q2_MEMORY_RECOVERY_NO_HBM_QUAL_FALSE_POSITIVE | 78.0 | Stage3-Yellow | 67.5 | Stage2-Watch | 1.95% | -42.71% | aligned_after_shadow |
| C06_SEC_202410_HBM3E_DELAY_HARD4C_PROTECTION | 60.0 | Stage2-Watch | 43.0 | Stage4C | 1.82% | -17.25% | aligned_after_shadow |


## 21. Coverage Matrix
| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C06_HBM_MEMORY_CUSTOMER_CAPACITY | HBM_MEMORY_CUSTOMER_QUALIFICATION_CAPACITY | 2 | 1 | 1 | 1 | 3 | 0 | 5 | 3 | 2 | true | true | C06 now has positive + counterexample + 4B/4C coverage; still needs non-Korean holdout or later batch validation if available |

## 22. Residual Contribution Summary
```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 2
same_archetype_new_symbol_count: 2
same_archetype_new_trigger_family_count: 4
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 4
positive_case_count: 2
counterexample_count: 1
current_profile_error_count: 2
diversity_score_summary: avg=24.0; C06 absent in local v12 coverage snapshot; two new symbols; four new trigger families; no representative duplicate reuse
tested_existing_calibrated_axes: stage2_actionable_evidence_bonus, stage3_green_revision_min, price_only_blowoff_blocks_positive_stage, full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
residual_error_types_found: generic_memory_recovery_false_positive_without_HBM_customer_quality; price_only_local_4B_too_early_for_SKH_structural_HBM; hard_4C_needed_after_customer_qualification_delay
new_axis_proposed: c06_customer_qualified_hbm_green_gate; c06_hbm_delay_hard4c_route
existing_axis_strengthened: full_4b_requires_non_price_evidence; hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: none
existing_axis_kept: stage2_actionable_evidence_bonus; stage3_green_revision_min; price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
auto_selected_coverage_gap: C06_HBM_MEMORY_CUSTOMER_CAPACITY absent in local v12 artifact snapshot
```

## 23. Validation Scope / Non-Validation Scope
Validated:
- Stock-web manifest and max date.
- Stock-web tradable OHLC rows for entry, peak, low, MFE/MAE windows.
- Symbol profiles and corporate-action window cleanliness.
- Historical event timing for HBM customer/capacity evidence using public sources.
- Positive/counterexample balance with representative trigger dedupe.

Not validated:
- Production scoring code.
- Any current/live candidate list.
- Any broker/API/autotrading route.
- Exact official intraday disclosure timestamp; entries use next-day or same-day close according to timing uncertainty noted in each trigger.
- Full 2Y MFE/MAE for all rows; 2Y fields are left null where not necessary for the C06 shadow rule.

## 24. Shadow Weight Calibration
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c06_customer_qualified_hbm_green_gate,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"Require durable HBM customer qualification / booked capacity for Green; generic memory recovery is insufficient","Samsung false-positive demoted; SKH positives retained","C06_SKH_202310_Q3_HBM_CUSTOMER_TRACTION_STAGE2A|C06_SKH_202404_Q1_HBM_SOLD_OUT_REVISION_GREEN|C06_SEC_202407_Q2_MEMORY_RECOVERY_NO_HBM_QUAL_FALSE_POSITIVE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c06_price_only_local_4b_overlay_guard,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"Local price peak without revision/customer deterioration should remain overlay-only","SKH 2024 local peak not treated as full 4B because full-window proximity is low","C06_SKH_202407_PRICE_ONLY_LOCAL_4B_OVERLAY",1,1,0,medium,canonical_shadow_only,"strengthens existing full_4b_requires_non_price_evidence"
shadow_weight,c06_hbm_delay_hard4c_route,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"Customer qualification delay / failed HBM3E conversion is thesis break, not price noise","Samsung 2024 hard4C row catches follow-on drawdown","C06_SEC_202410_HBM3E_DELAY_HARD4C_PROTECTION",1,1,1,medium,canonical_shadow_only,"routes qualification failure to 4C"
```

## 25. Machine-Readable Rows
### 25.1 price_source_validation
```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
```

### 25.2 case rows
```jsonl
{"row_type":"case","case_id":"C06_SKH_202310_Q3_HBM_CUSTOMER_TRACTION","symbol":"000660","company_name":"SK하이닉스","round":"R13","loop":"58","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_MEMORY_CUSTOMER_QUALIFICATION_CAPACITY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C06_SKH_202310_Q3_HBM_CUSTOMER_TRACTION_STAGE2A","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive MFE/MAE alignment","current_profile_verdict":"current_profile_missed_structural","price_source":"Songdaiki/stock-web","notes":"Early HBM/customer traction before later financial confirmation."}
{"row_type":"case","case_id":"C06_SKH_202404_Q1_HBM_SOLD_OUT_REVISION_GREEN","symbol":"000660","company_name":"SK하이닉스","round":"R13","loop":"58","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_MEMORY_CUSTOMER_QUALIFICATION_CAPACITY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"C06_SKH_202404_Q1_HBM_SOLD_OUT_REVISION_GREEN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"positive MFE/MAE alignment","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"HBM sold-out / booked-out capacity plus Q1 profit bridge."}
{"row_type":"case","case_id":"C06_SEC_202407_Q2_MEMORY_RECOVERY_NO_HBM_QUAL_FALSE_POSITIVE","symbol":"005930","company_name":"삼성전자","round":"R13","loop":"58","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_MEMORY_CUSTOMER_QUALIFICATION_CAPACITY","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"C06_SEC_202407_Q2_MEMORY_RECOVERY_NO_HBM_QUAL_FALSE_POSITIVE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"negative false-positive alignment","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Memory recovery without durable HBM customer qualification; later hard 4C evidence."}
```

### 25.3 trigger rows
```jsonl
{"row_type":"trigger","trigger_id":"C06_SKH_202310_Q3_HBM_CUSTOMER_TRACTION_STAGE2A","case_id":"C06_SKH_202310_Q3_HBM_CUSTOMER_TRACTION","symbol":"000660","company_name":"SK하이닉스","round":"R13","loop":"58","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_MEMORY_CUSTOMER_QUALIFICATION_CAPACITY","sector":"AI semiconductors / memory","primary_archetype":"HBM memory customer capacity","loop_objective":"coverage_gap_fill; residual_false_positive_mining; sector_specific_rule_discovery; canonical_archetype_compression; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2023-10-26","entry_date":"2023-10-27","entry_price":119100,"evidence_available_at_that_date":"Q3-2023 HBM / AI-memory traction became visible while shares were still below later HBM-cycle repricing.","evidence_source":"Reuters/press coverage on AI-HBM demand; stock-web 2023/2024 tradable shards","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","financial_visibility","durable_customer_confirmation"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000660/2023.csv|atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv","profile_path":"atlas/symbol_profiles/000/000660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":13.01,"MFE_90D_pct":46.85,"MFE_180D_pct":108.65,"MFE_1Y_pct":108.65,"MFE_2Y_pct":null,"MAE_30D_pct":-2.35,"MAE_90D_pct":-2.35,"MAE_180D_pct":-2.35,"MAE_1Y_pct":-2.35,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":248500,"drawdown_after_peak_pct":-16.7,"green_lateness_ratio":0.4536,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"high_mfe_low_mae_structural_success","current_profile_verdict":"current_profile_missed_structural","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_no_2023_2024_candidate_dates","same_entry_group_id":"C06_SKH_202310_000660_20231027_119100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C06_SKH_202404_Q1_HBM_SOLD_OUT_REVISION_GREEN","case_id":"C06_SKH_202404_Q1_HBM_SOLD_OUT_REVISION_GREEN","symbol":"000660","company_name":"SK하이닉스","round":"R13","loop":"58","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_MEMORY_CUSTOMER_QUALIFICATION_CAPACITY","sector":"AI semiconductors / memory","primary_archetype":"HBM memory customer capacity","loop_objective":"coverage_gap_fill; residual_false_positive_mining; sector_specific_rule_discovery; canonical_archetype_compression; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test","trigger_type":"Stage3-Green","trigger_date":"2024-04-25","entry_date":"2024-04-26","entry_price":177800,"evidence_available_at_that_date":"Q1-2024 earnings surprise plus HBM sold-out / booked-out capacity converted the earlier HBM thesis into financial visibility.","evidence_source":"Reuters Q1-2024 earnings; WSJ HBM sold-out coverage; stock-web 2024 tradable shard","stage2_evidence_fields":["public_event_or_disclosure","customer_or_order_quality","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["confirmed_revision","margin_bridge","multiple_public_sources","financial_visibility","durable_customer_confirmation","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv","profile_path":"atlas/symbol_profiles/000/000660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":18.11,"MFE_90D_pct":39.76,"MFE_180D_pct":39.76,"MFE_1Y_pct":39.76,"MFE_2Y_pct":null,"MAE_30D_pct":-4.95,"MAE_90D_pct":-14.74,"MAE_180D_pct":-18.62,"MAE_1Y_pct":-18.62,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":248500,"drawdown_after_peak_pct":-41.77,"green_lateness_ratio":0.0,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"green_confirmed_after_revision_still_positive","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_no_2024_candidate_dates","same_entry_group_id":"C06_SKH_202404_000660_20240426_177800","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C06_SKH_202407_PRICE_ONLY_LOCAL_4B_OVERLAY","case_id":"C06_SKH_202404_Q1_HBM_SOLD_OUT_REVISION_GREEN","symbol":"000660","company_name":"SK하이닉스","round":"R13","loop":"58","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_MEMORY_CUSTOMER_QUALIFICATION_CAPACITY","sector":"AI semiconductors / memory","primary_archetype":"HBM memory customer capacity","loop_objective":"coverage_gap_fill; residual_false_positive_mining; sector_specific_rule_discovery; canonical_archetype_compression; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test","trigger_type":"Stage4B-Overlay","trigger_date":"2024-07-11","entry_date":"2024-07-11","entry_price":241000,"evidence_available_at_that_date":"Local price peak after HBM rally, but no thesis-breaking non-price evidence; later stock-web profile shows structurally higher later prices, so full 4B should not be price-only.","evidence_source":"stock-web 2024 shard and profile latest-close stress test","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["valuation_blowoff","price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv","profile_path":"atlas/symbol_profiles/000/000660.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":3.11,"MFE_90D_pct":3.11,"MFE_180D_pct":3.11,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-37.1,"MAE_90D_pct":-39.96,"MAE_180D_pct":-39.96,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":248500,"drawdown_after_peak_pct":-41.77,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.894,"four_b_full_window_peak_proximity":0.082,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"not_applicable","trigger_outcome_label":"local_peak_but_not_full_window_4B","current_profile_verdict":"current_profile_4B_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_no_2024_candidate_dates","same_entry_group_id":"C06_SKH_202407_000660_20240711_241000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":true,"reuse_reason":"same_symbol_new_4B_trigger_family","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C06_SEC_202407_Q2_MEMORY_RECOVERY_NO_HBM_QUAL_FALSE_POSITIVE","case_id":"C06_SEC_202407_Q2_MEMORY_RECOVERY_NO_HBM_QUAL_FALSE_POSITIVE","symbol":"005930","company_name":"삼성전자","round":"R13","loop":"58","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_MEMORY_CUSTOMER_QUALIFICATION_CAPACITY","sector":"AI semiconductors / memory","primary_archetype":"HBM memory customer capacity","loop_objective":"coverage_gap_fill; residual_false_positive_mining; sector_specific_rule_discovery; canonical_archetype_compression; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-05","entry_date":"2024-07-05","entry_price":87100,"evidence_available_at_that_date":"Generic memory recovery / AI-memory expectation at Q2 preliminary results without durable HBM3E customer qualification evidence; subsequent HBM delay evidence validated the red-team gap.","evidence_source":"Reuters May 2024 HBM qualification issue; Reuters Oct 2024 HBM3E delay; stock-web 2024/2025 shards","stage2_evidence_fields":["public_event_or_disclosure","relative_strength","early_revision_signal"],"stage3_evidence_fields":["financial_visibility"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":["qualification_failure","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv|atlas/ohlcv_tradable_by_symbol_year/005/005930/2025.csv","profile_path":"atlas/symbol_profiles/005/005930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.95,"MFE_90D_pct":1.95,"MFE_180D_pct":1.95,"MFE_1Y_pct":1.95,"MFE_2Y_pct":null,"MAE_30D_pct":-19.4,"MAE_90D_pct":-42.71,"MAE_180D_pct":-42.71,"MAE_1Y_pct":-42.71,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-11","peak_price":88800,"drawdown_after_peak_pct":-43.81,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":[],"four_c_protection_label":"thesis_break_watch_only_before_hard_4C","trigger_outcome_label":"false_positive_memory_recovery_without_hbm_customer_quality","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_no_2024_2025_candidate_dates","same_entry_group_id":"C06_SEC_202407_005930_20240705_87100","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"C06_SEC_202410_HBM3E_DELAY_HARD4C_PROTECTION","case_id":"C06_SEC_202407_Q2_MEMORY_RECOVERY_NO_HBM_QUAL_FALSE_POSITIVE","symbol":"005930","company_name":"삼성전자","round":"R13","loop":"58","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","fine_archetype_id":"HBM_MEMORY_CUSTOMER_QUALIFICATION_CAPACITY","sector":"AI semiconductors / memory","primary_archetype":"HBM memory customer capacity","loop_objective":"coverage_gap_fill; residual_false_positive_mining; sector_specific_rule_discovery; canonical_archetype_compression; 4B_non_price_requirement_stress_test; 4C_thesis_break_timing_test","trigger_type":"Stage4C","trigger_date":"2024-10-08","entry_date":"2024-10-08","entry_price":60300,"evidence_available_at_that_date":"Samsung apologized for Q3 profit miss and disclosed delayed sales of high-end HBM3E chips to a major customer; this is not mere price weakness but customer-qualification thesis break.","evidence_source":"Reuters Oct-2024 Samsung apology / HBM3E delay; stock-web 2024 shard","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["revision_slowdown","margin_or_backlog_slowdown"],"stage4c_evidence_fields":["qualification_failure","thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv|atlas/ohlcv_tradable_by_symbol_year/005/005930/2025.csv","profile_path":"atlas/symbol_profiles/005/005930.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","MFE_30D_pct":1.82,"MFE_90D_pct":1.82,"MFE_180D_pct":2.32,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-17.25,"MAE_90D_pct":-17.25,"MAE_180D_pct":-17.25,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-10-15","peak_price":61400,"drawdown_after_peak_pct":-18.73,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_applicable","four_b_evidence_type":["revision_slowdown","margin_or_backlog_slowdown"],"four_c_protection_label":"hard_4c_success","trigger_outcome_label":"hard_4c_protected_against_follow_on_drawdown","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window_no_2024_2025_candidate_dates","same_entry_group_id":"C06_SEC_202410_005930_20241008_60300","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":true,"reuse_reason":"same_symbol_new_4C_trigger_family","independent_evidence_weight":0.5,"do_not_count_as_new_case":false}
```

### 25.4 score_simulation rows
```jsonl
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_SKH_202310_Q3_HBM_CUSTOMER_TRACTION","trigger_id":"C06_SKH_202310_Q3_HBM_CUSTOMER_TRACTION_STAGE2A","symbol":"000660","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":6,"margin_bridge_score":5,"revision_score":7,"relative_strength_score":6,"customer_quality_score":8,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":83.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":7,"margin_bridge_score":6,"revision_score":8,"relative_strength_score":7,"customer_quality_score":9,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":88.5,"stage_label_after":"Stage3-Green","changed_components":["customer_quality_score","capacity_or_shipment_score","execution_risk_score"],"component_delta_explanation":"C06 shadow profile raises customer-qualified HBM/capacity evidence weight and penalizes generic memory recovery without durable customer qualification. Price-only local peaks remain overlay-only.","MFE_90D_pct":46.85,"MAE_90D_pct":-2.35,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_missed_structural"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_SKH_202404_Q1_HBM_SOLD_OUT_REVISION_GREEN","trigger_id":"C06_SKH_202404_Q1_HBM_SOLD_OUT_REVISION_GREEN","symbol":"000660","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":8,"margin_bridge_score":8,"revision_score":9,"relative_strength_score":8,"customer_quality_score":9,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":90.0,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":9,"margin_bridge_score":9,"revision_score":10,"relative_strength_score":8,"customer_quality_score":10,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":2,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":94.0,"stage_label_after":"Stage3-Green","changed_components":["customer_quality_score","capacity_or_shipment_score","execution_risk_score"],"component_delta_explanation":"C06 shadow profile raises customer-qualified HBM/capacity evidence weight and penalizes generic memory recovery without durable customer qualification. Price-only local peaks remain overlay-only.","MFE_90D_pct":39.76,"MAE_90D_pct":-14.74,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_SKH_202404_Q1_HBM_SOLD_OUT_REVISION_GREEN","trigger_id":"C06_SKH_202407_PRICE_ONLY_LOCAL_4B_OVERLAY","symbol":"000660","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":9,"relative_strength_score":10,"customer_quality_score":9,"policy_or_regulatory_score":0,"valuation_repricing_score":9,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":92.0,"stage_label_before":"Stage3-Green+PriceOverheatWatch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":9,"relative_strength_score":10,"customer_quality_score":9,"policy_or_regulatory_score":0,"valuation_repricing_score":8,"execution_risk_score":3,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":90.0,"stage_label_after":"Stage3-Green+Local4BWatch","changed_components":["customer_quality_score","capacity_or_shipment_score","execution_risk_score"],"component_delta_explanation":"C06 shadow profile raises customer-qualified HBM/capacity evidence weight and penalizes generic memory recovery without durable customer qualification. Price-only local peaks remain overlay-only.","MFE_90D_pct":3.11,"MAE_90D_pct":-39.96,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_4B_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_SEC_202407_Q2_MEMORY_RECOVERY_NO_HBM_QUAL_FALSE_POSITIVE","trigger_id":"C06_SEC_202407_Q2_MEMORY_RECOVERY_NO_HBM_QUAL_FALSE_POSITIVE","symbol":"005930","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":6,"revision_score":7,"relative_strength_score":7,"customer_quality_score":3,"policy_or_regulatory_score":0,"valuation_repricing_score":7,"execution_risk_score":5,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":78.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":5,"revision_score":6,"relative_strength_score":6,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":5,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":67.5,"stage_label_after":"Stage2-Watch","changed_components":["customer_quality_score","capacity_or_shipment_score","execution_risk_score"],"component_delta_explanation":"C06 shadow profile raises customer-qualified HBM/capacity evidence weight and penalizes generic memory recovery without durable customer qualification. Price-only local peaks remain overlay-only.","MFE_90D_pct":1.95,"MAE_90D_pct":-42.71,"score_return_alignment_label":"current_profile_misaligned_after_guard_aligned","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"C06_SEC_202407_Q2_MEMORY_RECOVERY_NO_HBM_QUAL_FALSE_POSITIVE","trigger_id":"C06_SEC_202410_HBM3E_DELAY_HARD4C_PROTECTION","symbol":"005930","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":4,"revision_score":5,"relative_strength_score":2,"customer_quality_score":1,"policy_or_regulatory_score":0,"valuation_repricing_score":3,"execution_risk_score":8,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_before":60.0,"stage_label_before":"Stage2-Watch","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":2,"revision_score":2,"relative_strength_score":1,"customer_quality_score":0,"policy_or_regulatory_score":0,"valuation_repricing_score":1,"execution_risk_score":9,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0},"weighted_score_after":43.0,"stage_label_after":"Stage4C","changed_components":["customer_quality_score","capacity_or_shipment_score","execution_risk_score"],"component_delta_explanation":"C06 shadow profile raises customer-qualified HBM/capacity evidence weight and penalizes generic memory recovery without durable customer qualification. Price-only local peaks remain overlay-only.","MFE_90D_pct":1.82,"MAE_90D_pct":-17.25,"score_return_alignment_label":"aligned","current_profile_verdict":"current_profile_4C_too_late"}
```

### 25.5 shadow_weight rows
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c06_customer_qualified_hbm_green_gate,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"Require durable HBM customer qualification / booked capacity for Green; generic memory recovery is insufficient","Samsung false-positive demoted; SKH positives retained","C06_SKH_202310_Q3_HBM_CUSTOMER_TRACTION_STAGE2A|C06_SKH_202404_Q1_HBM_SOLD_OUT_REVISION_GREEN|C06_SEC_202407_Q2_MEMORY_RECOVERY_NO_HBM_QUAL_FALSE_POSITIVE",3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c06_price_only_local_4b_overlay_guard,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"Local price peak without revision/customer deterioration should remain overlay-only","SKH 2024 local peak not treated as full 4B because full-window proximity is low","C06_SKH_202407_PRICE_ONLY_LOCAL_4B_OVERLAY",1,1,0,medium,canonical_shadow_only,"strengthens existing full_4b_requires_non_price_evidence"
shadow_weight,c06_hbm_delay_hard4c_route,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"Customer qualification delay / failed HBM3E conversion is thesis break, not price noise","Samsung 2024 hard4C row catches follow-on drawdown","C06_SEC_202410_HBM3E_DELAY_HARD4C_PROTECTION",1,1,1,medium,canonical_shadow_only,"routes qualification failure to 4C"
```

### 25.6 residual_contribution row
```jsonl
{"row_type":"residual_contribution","round":"R13","loop":"58","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":2,"same_archetype_new_symbol_count":2,"same_archetype_new_trigger_family_count":4,"new_canonical_archetype_count":1,"new_trigger_family_count":4,"positive_case_count":2,"counterexample_count":1,"current_profile_error_count":2,"diversity_score_summary":"avg=24.0; C06 was absent in local v12 coverage snapshot; two new symbols and four new trigger families; no representative duplicate reuse","tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["generic_memory_recovery_false_positive_without_HBM_customer_quality","price_only_local_4B_too_early_for_SKH_structural_HBM","hard_4C_needed_after_customer_qualification_delay"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false,"auto_selected_coverage_gap":"C06_HBM_MEMORY_CUSTOMER_CAPACITY absent in /mnt/data v12 artifact snapshot"}
```

### 25.7 narrative_only rows
```jsonl
{"row_type":"narrative_only","case_id":"C06_FUTURE_HOLDOUT_SAMSUNG_2025_HBM_RECOVERY","symbol":"005930","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C06_HBM_MEMORY_CUSTOMER_CAPACITY","reason":"future_or_later_evidence_window_not_used_for_weight_calibration_in_this_loop","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
next_round = R13_loop_59
auto_selected_coverage_gap_after_this_loop = C01/C02/C03/C05/C08/C10/C11/C12/C13 remain candidates depending on local artifact promotion state
recommended_next = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY or C11_BATTERY_ORDERBOOK_RERATING
avoid_next_duplicate = C06 same SKH 2023-10-27 / SKH 2024-04-26 / Samsung 2024-07-05 triggers
```

## 28. Source Notes
- Stock-Web manifest and price/profile data: Songdaiki/stock-web fetched from `atlas/manifest.json`, symbol profiles, and tradable symbol-year CSV shards. fileciteturn973file0 fileciteturn977file0 fileciteturn978file0 fileciteturn981file0
- SK하이닉스 2024 evidence: Reuters Q1 2024 AI/HBM earnings report and WSJ HBM sold-out coverage. citeturn791384news1 citeturn287683news5
- 삼성전자 counterexample evidence: Reuters May 2024 Nvidia qualification failure report and Reuters October 2024 HBM3E delay / apology report. citeturn791384news0 citeturn501556news0
- OHLC calculations use raw/unadjusted stock-web tradable rows; no adjusted-price route was used.
