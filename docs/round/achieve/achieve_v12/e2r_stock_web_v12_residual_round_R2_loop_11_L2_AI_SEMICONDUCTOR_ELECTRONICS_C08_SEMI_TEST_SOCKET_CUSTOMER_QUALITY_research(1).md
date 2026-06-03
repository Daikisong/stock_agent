# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```json
{
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "scheduled_round": "R2",
  "scheduled_loop": 11,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R2",
  "completed_loop": 11,
  "next_round": "R3",
  "next_loop": 11,
  "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS",
  "canonical_archetype_id": "C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY",
  "fine_archetype_id": "SEMI_TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_AI_EDGE_DEVICE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "green_strictness_stress_test",
    "yellow_threshold_stress_test",
    "4B_non_price_requirement_stress_test",
    "4C_thesis_break_timing_test",
    "sector_specific_rule_discovery",
    "canonical_archetype_compression"
  ],
  "price_source": "Songdaiki/stock-web",
  "stock_web_manifest_max_date": "2026-02-20",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "new_independent_case_count": 3,
  "reused_case_count": 0,
  "new_symbol_count": 3,
  "same_archetype_new_symbol_count": 3,
  "same_archetype_new_trigger_family_count": 3,
  "new_trigger_family_count": 3,
  "calibration_usable_case_count": 3,
  "calibration_usable_trigger_count": 6,
  "positive_case_count": 2,
  "counterexample_count": 1,
  "current_profile_error_count": 2,
  "diversity_score_summary": "estimated +38; wrong_round_penalty=0; repeated_same_symbol_penalty=0; schema_rematerialization_penalty=0",
  "loop_contribution_label": "canonical_archetype_rule_candidate",
  "do_not_propose_new_weight_delta": false
}
```

This loop adds 3 new independent cases, 1 counterexamples, and 2 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY.

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

This file does not change production scoring. All rule candidates are shadow-only.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R2
scheduled_loop = 11
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
fine_archetype_id = SEMI_TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_AI_EDGE_DEVICE
round_schedule_status = valid
round_sector_consistency = pass
```

R2 covers AI, semiconductors, semiconductor equipment, advanced electronics and electronic components. This loop deliberately avoids repeating the common HBM equipment representative set and instead focuses on the test-socket / probe-card customer-quality axis.

## 3. Previous Coverage / Duplicate Avoidance Check

The prior chat-generated artifact ended with `next_round=R2 / next_loop=11`, so this file follows that scheduler state. The allowed `stock_agent` artifact registry was inspected only for duplicate-avoidance context and not used to open or infer production code.

```text
same_canonical_archetype_research = allowed
same_symbol_same_trigger_date_research = avoided
new_symbol_count = 3
same_archetype_new_symbol_count = 3
same_archetype_new_trigger_family_count = 3
new_independent_case_ratio = 1.00
wrong_round_penalty = 0
```

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_data_source = Songdaiki/stock-web
source_basis = FinanceData/marcap
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
raw_shard_root = atlas/ohlcv_raw_by_symbol_year
```

Symbol profile checks:

| symbol | company | profile path | corporate action status for chosen window |
|---:|---|---|---|
| 058470 | 리노공업 | atlas/symbol_profiles/058/058470.json | 2025-04-25 candidate is outside 2024 Jan~Oct 180D window |
| 131290 | 티에스이 | atlas/symbol_profiles/131/131290.json | corporate-action candidates are 2011 only, outside window |
| 095340 | ISC | atlas/symbol_profiles/095/095340.json | 2023-10-20 candidate avoided by using post-2024 window |

## 5. Historical Eligibility Gate

```text
trigger_date is historical = true
entry_date exists in stock-web tradable shard = true
forward 180D trading window available = true
required OHLC fields available = true
corporate_action_contaminated_180D_window = false
calibration_usable = true
```

All representative triggers use 2024 windows and stay before the stock-web manifest max date.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | Compression logic |
|---|---|---|
| SEMI_TEST_SOCKET_PROBE_PIN_AI_EDGE_DEVICE | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | Test-socket/probe-pin scarcity, customer-quality franchise and edge-AI/advanced logic demand. |
| SEMI_TEST_PROBE_CARD_HBM_INTERFACE_QUALITY | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | Probe-card/test interface quality in advanced memory/HBM value chain. |
| SEMI_TEST_SOCKET_HBM_NARRATIVE_BLOWOFF | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | Same socket narrative, but price-only overheat without fresh customer/revision proof. |

## 7. Case Selection Summary

| case_id | symbol | company | role | why selected |
|---|---:|---|---|---|
| R2L11_C08_058470_RINO_AI_TEST_SOCKET | 058470 | 리노공업 | high_mae_success | Positive C08 case where Stage2/Yellow caught large upside, but late Green/4B mattered. |
| R2L11_C08_131290_TSE_HBM_PROBE_CARD | 131290 | 티에스이 | high_mae_success | Positive C08 case with strong MFE but severe later drawdown, requiring high-MAE treatment. |
| R2L11_C08_095340_ISC_SOCKET_BLOWOFF | 095340 | ISC | false_positive_green | Counterexample where price-only socket/HBM narrative had low MFE and very high MAE. |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
calibration_usable_case_count = 3
4B_case_count = 2
4C_case_count = 1
```

The positive cases show that C08 should not be ignored. The counterexample shows that customer-quality language becomes dangerous when it is no longer backed by fresh revision, customer-mix proof, or margin/utilization bridge.

## 9. Evidence Source Map

| symbol | evidence family | evidence timing | validation status |
|---:|---|---|---|
| 058470 | AI edge device / advanced logic test socket franchise | 2024-01~2024-05 | public-source summary; exact URL enrichment required |
| 131290 | HBM/probe-card/test interface quality narrative | 2024-02~2024-05 | public-source summary; exact URL enrichment required |
| 095340 | HBM/socket relative-strength blowoff after 2023 corporate-action candidate | 2024-03~2024-08 | public-source summary; exact URL enrichment required |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path | entry_date | forward window |
|---:|---|---|---|---|
| 058470 | atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv | atlas/symbol_profiles/058/058470.json | 2024-01-10 | usable |
| 131290 | atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv | atlas/symbol_profiles/131/131290.json | 2024-02-13 | usable |
| 095340 | atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv | atlas/symbol_profiles/095/095340.json | 2024-03-08 | usable |

## 11. Case-by-Case Trigger Grid

| case | symbol | trigger | entry | entry_price | MFE_30 | MFE_90 | MFE_180 | MAE_30 | MAE_90 | MAE_180 | verdict |
|---|---:|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| 리노공업 AI/test socket | 058470 | Stage2-Actionable | 2024-01-10 | 209,000 | +14.11% | +47.85% | +47.85% | -10.10% | -10.10% | -21.53% | high-MAE structural success |
| 티에스이 HBM probe-card | 131290 | Stage2-Actionable | 2024-02-13 | 57,000 | +10.88% | +54.04% | +54.04% | -8.42% | -8.42% | -33.25% | high-MAE structural success |
| ISC socket blowoff | 095340 | Stage3-Green-FalsePositive | 2024-03-08 | 95,000 | +13.68% | +13.68% | +13.68% | -12.63% | -38.21% | -56.74% | counterexample / false Green |


## 12. Trigger-Level OHLC Backtest Tables

Representative aggregate:

| metric | 058470 | 131290 | 095340 |
|---|---:|---:|---:|
| entry_price | 209,000 | 57,000 | 95,000 |
| MFE_30D_pct | +14.11 | +10.88 | +13.68 |
| MFE_90D_pct | +47.85 | +54.04 | +13.68 |
| MFE_180D_pct | +47.85 | +54.04 | +13.68 |
| MAE_30D_pct | -10.10 | -8.42 | -12.63 |
| MAE_90D_pct | -10.10 | -8.42 | -38.21 |
| MAE_180D_pct | -21.53 | -33.25 | -56.74 |

Aggregate representative metric:

```text
positive_avg_MFE_180D_pct = 50.95
positive_avg_MAE_180D_pct = -27.39
counterexample_MFE_180D_pct = 13.68
counterexample_MAE_180D_pct = -56.74
```

## 13. Current Calibrated Profile Stress Test

| case | current profile likely label | actual result | verdict |
|---|---|---|---|
| 058470 리노공업 | Stage2/Yellow; Green confirmation may arrive late | MFE was large, but late-Green around May was near peak | current_profile_too_late |
| 131290 티에스이 | Stage2/Yellow, not automatic Green | Good MFE with severe later MAE | current_profile_correct |
| 095340 ISC | could be overpromoted if socket/HBM relative strength is treated as Green | low MFE and severe MAE | current_profile_false_positive |

Axis verdict:

```text
stage2_actionable_evidence_bonus = existing_axis_tested
stage3_yellow_total_min = existing_axis_kept
stage3_green_total_min = existing_axis_strengthened for C08 if fresh revision/customer proof is missing
stage3_green_revision_min = existing_axis_strengthened
price_only_blowoff_blocks_positive_stage = existing_axis_strengthened
full_4b_requires_non_price_evidence = existing_axis_strengthened
hard_4c_thesis_break_routes_to_4c = existing_axis_kept
```

## 14. Stage2 / Yellow / Green Comparison

C08 needs a more surgical split:

```text
Stage2-Actionable:
  customer-quality franchise + relative strength + early revision/sales route

Stage3-Yellow:
  same evidence plus financial visibility, repeatable demand, and low accounting/trust risk

Stage3-Green:
  fresh revision/customer bridge, margin or utilization proof, and not price-only blowoff
```

Late Green is dangerous in C08 because a socket/probe-card rerating often travels fast. Once the market starts treating customer quality as scarcity, the stock can become a stretched spring: it still points in the correct direction, but the remaining upside may be small while the downside energy is already stored.

## 15. 4B Local vs Full-window Timing Audit

| trigger | local_peak_proximity | full_window_peak_proximity | verdict |
|---|---:|---:|---|
| RINO 2024-05-07 | 0.89 | 0.89 | good_full_window_4B_timing_if_non_price_evidence_confirmed |
| TSE 2024-04-26 | 0.71 | 0.71 | late_green_near_full_window_peak |
| ISC 2024-03-08 false Green | 0.31 | 0.31 | not full 4B yet, but overpromotion risk already high |

## 16. 4C Protection Audit

ISC shows why hard 4C should not be triggered from price-only collapse alone. The 2024-08-05 washout was near a local capitulation, and a price-only hard 4C could have been a false break. C08 therefore needs:

```text
hard_4c = confirmed customer loss OR utilization/margin thesis break OR accounting/trust break
price_only_large_MAE = 4C_watch_only
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = sector_specific
large_sector_id = L2_AI_SEMICONDUCTOR_ELECTRONICS
candidate_axis = test_socket_customer_quality_yellow_not_green
```

Candidate rule:

```text
For L2 test-socket/probe-card cases, reward repeatable customer-quality franchise and early revision
with Yellow promotion, but block Green if the evidence is mostly price-only scarcity narrative or if
valuation/positioning is already overheated.
```

## 18. Canonical-Archetype Rule Candidate

```text
rule_scope = canonical_archetype_specific
canonical_archetype_id = C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY
new_axis_proposed =
  c08_repeatable_customer_quality_yellow_bonus
  c08_green_requires_revision_customer_bridge
  c08_price_only_socket_blowoff_overlay_only
```

## 19. Before / After Backtest Comparison

| profile | selected triggers | avg_MFE_90D | avg_MAE_90D | avg_MFE_180D | avg_MAE_180D | false_positive_rate | missed_structural_count | late_green_count | avg_green_lateness_ratio | score_return_alignment_verdict |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | +38.52 | -18.91 | +38.52 | -37.17 | 0.33 | 0 | 2 | 0.64 | acceptable but ISC false Green remains |
| P0b e2r_2_0_baseline_reference | 3 | +38.52 | -18.91 | +38.52 | -37.17 | 0.33 | 0 | 2 | 0.64 | too blunt; customer quality and price momentum blur |
| P1 sector_specific_candidate_profile | 3 | +50.95 promoted / +13.68 capped | -9.26 promoted / -38.21 capped | +50.95 promoted | -27.39 promoted | 0.00 | 0 | 1 | 0.80 | better separation |
| P2 canonical_archetype_candidate_profile | 3 | +50.95 promoted / +13.68 capped | -9.26 promoted / -38.21 capped | +50.95 promoted | -27.39 promoted | 0.00 | 0 | 1 | 0.80 | best explanatory fit |
| P3 counterexample_guard_profile | 3 | +38.52 | -18.91 | +38.52 | -37.17 | 0.00 Green false-positive | 0 | 2 | 0.64 | conservative; may keep too much at Yellow |

## 20. Score-Return Alignment Matrix

| case | weighted_score_before | stage_before | weighted_score_after | stage_after | alignment |
|---|---:|---|---:|---|---|
| 058470 | 74.0 | Stage2-Actionable | 79.0 | Stage3-Yellow | Yellow aligned; Green too late near peak |
| 131290 | 72.0 | Stage2-Actionable | 77.0 | Stage3-Yellow | Yellow aligned; high-MAE success guard needed |
| 095340 | 83.0 | Stage3-Green | 68.0 | Stage2-Watch | cap aligned with low MFE/high MAE counterexample |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY | SEMI_TEST_SOCKET_PROBE_CARD_CUSTOMER_QUALITY_AI_EDGE_DEVICE | 2 | 1 | 2 | 1 | 3 | 0 | 6 | 3 | 2 | true | true | C08 now has positive high-MAE successes and one price-only false-Green counterexample; needs exact evidence URL enrichment and non-2024 holdout cases. |


## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 3
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - stage3_cross_evidence_green_buffer
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - price_only_socket_blowoff_false_green
  - late_green_after_most_upside_captured
  - high_MAE_success_needs_yellow_not_green
  - hard_4c_price_only_false_break_risk
new_axis_proposed:
  - c08_repeatable_customer_quality_yellow_bonus
  - c08_green_requires_revision_customer_bridge
  - c08_price_only_socket_blowoff_overlay_only
existing_axis_strengthened:
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- stock-web manifest and price basis
- profile availability for 058470, 131290, 095340
- representative entry prices from stock-web tradable shards
- 30D/90D/180D MFE/MAE proxy calculations
- clean 180D corporate-action windows for selected triggers
- R2/L2/C08 schedule consistency
```

Not validated:

```text
- production scoring code
- live watchlist
- brokerage execution
- exact original disclosure/report URLs for each evidence row
- post-2026-02-20 price path
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c08_repeatable_customer_quality_yellow_bonus,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,+1.5,+1.5,"Repeatable test-socket/probe-card franchise plus relative strength and early revision supports Yellow, not immediate Green","positive rows avg 180D MFE 50.95 pct but avg 180D MAE -27.39 pct","R2L11_T01_RINO_STAGE2_TEST_SOCKET_AI_EDGE_DEVICE|R2L11_T02_TSE_STAGE2_HBM_PROBE_CARD_QUALITY",3,3,1,medium,canonical_shadow_only,"not production; requires exact source URL enrichment"
shadow_weight,c08_green_requires_revision_customer_bridge,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,-2,-2,"Green should require fresh revision/customer bridge; socket quality alone is insufficient after sharp price rerating","blocks ISC false Green; preserves RINO/TSE as Yellow/high-MAE successes","R2L11_T03_ISC_STAGE3_FALSE_GREEN_SOCKET_BLOWOFF",3,3,1,medium,canonical_shadow_only,"strengthens existing Green strictness only for C08"
shadow_weight,c08_price_only_socket_blowoff_overlay_only,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY,0,1,+1,"Price-only HBM/socket blowoff is 4B overlay, not positive Stage3 evidence","helps separate Leeno/TSE late Green and ISC false positive","R2L11_T01B_RINO_LATE_GREEN_4B_OVERLAY|R2L11_T02B_TSE_LATE_GREEN_4B_OVERLAY|R2L11_T03B_ISC_4C_WATCH_AFTER_BLOWOFF",3,3,1,low,guardrail_shadow_only,"overlay/risk calibration only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R2L11_C08_058470_RINO_AI_TEST_SOCKET","symbol":"058470","company_name":"리노공업","round":"R2","loop":"11","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMI_TEST_SOCKET_PROBE_PIN_AI_EDGE_DEVICE","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R2L11_T01_RINO_STAGE2_TEST_SOCKET_AI_EDGE_DEVICE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Stage2/Yellow captures the move; late Green around May peak consumes most upside.","current_profile_verdict":"current_profile_too_late","price_source":"Songdaiki/stock-web","notes":"Customer-quality and test-socket scarcity narrative worked, but 4B/Green timing was very sensitive to valuation overheat."}
{"row_type":"case","case_id":"R2L11_C08_131290_TSE_HBM_PROBE_CARD","symbol":"131290","company_name":"티에스이","round":"R2","loop":"11","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMI_TEST_PROBE_CARD_HBM_INTERFACE_QUALITY","case_type":"high_mae_success","positive_or_counterexample":"positive","best_trigger":"R2L11_T02_TSE_STAGE2_HBM_PROBE_CARD_QUALITY","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Stage2/Yellow was rewarded; Green needs confirmation because 180D MAE/drawdown were severe.","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"Probe-card/test-interface quality signal was tradeable, but drawdown argues for high-MAE-success handling rather than unrestricted Green."}
{"row_type":"case","case_id":"R2L11_C08_095340_ISC_SOCKET_BLOWOFF","symbol":"095340","company_name":"ISC","round":"R2","loop":"11","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMI_TEST_SOCKET_HBM_NARRATIVE_BLOWOFF","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"R2L11_T03_ISC_STAGE3_FALSE_GREEN_SOCKET_BLOWOFF","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"Price-only HBM/test-socket rerating without fresh customer/revision bridge created a Green trap.","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"Useful residual counterexample: socket quality narrative alone should not override valuation/positioning overheat."}
{"row_type":"trigger","trigger_id":"R2L11_T01_RINO_STAGE2_TEST_SOCKET_AI_EDGE_DEVICE","case_id":"R2L11_C08_058470_RINO_AI_TEST_SOCKET","symbol":"058470","company_name":"리노공업","round":"R2","loop":"11","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMI_TEST_SOCKET_PROBE_PIN_AI_EDGE_DEVICE","sector":"AI·반도체·전자부품","primary_archetype":"semi test socket customer quality","loop_objective":"coverage_gap_fill|counterexample_mining|green_strictness_stress_test|yellow_threshold_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-01-10","evidence_available_at_that_date":"AI edge-device / advanced-logic test-socket scarcity narrative with high customer-quality franchise; not a direct new purchase order.","evidence_source":"public analyst/media summary; exact original URL enrichment required before production promotion","stage2_evidence_fields":["customer_or_order_quality","relative_strength","capacity_or_volume_route","early_revision_signal"],"stage3_evidence_fields":["financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":[],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv","profile_path":"atlas/symbol_profiles/058/058470.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-01-10","entry_price":209000,"MFE_30D_pct":14.11,"MFE_90D_pct":47.85,"MFE_180D_pct":47.85,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-10.1,"MAE_90D_pct":-10.1,"MAE_180D_pct":-21.53,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-07","peak_price":309000,"drawdown_after_peak_pct":-46.93,"green_lateness_ratio":0.89,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L11_058470_20240110_209000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L11_T01B_RINO_LATE_GREEN_4B_OVERLAY","case_id":"R2L11_C08_058470_RINO_AI_TEST_SOCKET","symbol":"058470","company_name":"리노공업","round":"R2","loop":"11","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMI_TEST_SOCKET_PROBE_PIN_AI_EDGE_DEVICE","sector":"AI·반도체·전자부품","primary_archetype":"semi test socket customer quality","loop_objective":"coverage_gap_fill|counterexample_mining|green_strictness_stress_test|yellow_threshold_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage4B-Overlay","trigger_date":"2024-05-07","evidence_available_at_that_date":"Price reached observed full-window peak after strong test-socket rerating; full 4B still requires valuation/revision/positioning evidence.","evidence_source":"public analyst/media summary; exact original URL enrichment required before production promotion","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","financial_visibility"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/058/058470/2024.csv","profile_path":"atlas/symbol_profiles/058/058470.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-05-07","entry_price":298000,"MFE_30D_pct":2.01,"MFE_90D_pct":2.01,"MFE_180D_pct":2.01,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-15.1,"MAE_90D_pct":-44.97,"MAE_180D_pct":-44.97,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-07","peak_price":309000,"drawdown_after_peak_pct":-46.93,"green_lateness_ratio":0.89,"four_b_local_peak_proximity":0.89,"four_b_full_window_peak_proximity":0.89,"four_b_timing_verdict":"good_full_window_4B_timing_if_non_price_evidence_confirmed","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_4B_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L11_058470_20240507_298000","dedupe_for_aggregate":false,"aggregate_group_role":"4B_overlay_only","is_new_independent_case":false,"reuse_reason":"same case 4B timing overlay, not aggregate representative","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R2L11_T02_TSE_STAGE2_HBM_PROBE_CARD_QUALITY","case_id":"R2L11_C08_131290_TSE_HBM_PROBE_CARD","symbol":"131290","company_name":"티에스이","round":"R2","loop":"11","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMI_TEST_PROBE_CARD_HBM_INTERFACE_QUALITY","sector":"AI·반도체·전자부품","primary_archetype":"semi test socket customer quality","loop_objective":"coverage_gap_fill|counterexample_mining|green_strictness_stress_test|yellow_threshold_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage2-Actionable","trigger_date":"2024-02-13","evidence_available_at_that_date":"HBM/probe-card/test-interface quality narrative became tradable, but not enough for unguarded Green because later MAE was severe.","evidence_source":"public analyst/media summary; exact original URL enrichment required before production promotion","stage2_evidence_fields":["customer_or_order_quality","relative_strength","early_revision_signal"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv","profile_path":"atlas/symbol_profiles/131/131290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-02-13","entry_price":57000,"MFE_30D_pct":10.88,"MFE_90D_pct":54.04,"MFE_180D_pct":54.04,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-8.42,"MAE_90D_pct":-8.42,"MAE_180D_pct":-33.25,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-03","peak_price":87800,"drawdown_after_peak_pct":-56.66,"green_lateness_ratio":0.71,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"high_mae_success","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L11_131290_20240213_57000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L11_T02B_TSE_LATE_GREEN_4B_OVERLAY","case_id":"R2L11_C08_131290_TSE_HBM_PROBE_CARD","symbol":"131290","company_name":"티에스이","round":"R2","loop":"11","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMI_TEST_PROBE_CARD_HBM_INTERFACE_QUALITY","sector":"AI·반도체·전자부품","primary_archetype":"semi test socket customer quality","loop_objective":"coverage_gap_fill|counterexample_mining|green_strictness_stress_test|yellow_threshold_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage3-Green-Late","trigger_date":"2024-04-26","evidence_available_at_that_date":"Late confirmation/price breakout after most of the TSE upside had already appeared.","evidence_source":"public analyst/media summary; exact original URL enrichment required before production promotion","stage2_evidence_fields":[],"stage3_evidence_fields":["confirmed_revision","multiple_public_sources","financial_visibility"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":[],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/131/131290/2024.csv","profile_path":"atlas/symbol_profiles/131/131290.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-04-26","entry_price":79000,"MFE_30D_pct":11.14,"MFE_90D_pct":11.14,"MFE_180D_pct":11.14,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-21.65,"MAE_90D_pct":-51.84,"MAE_180D_pct":-51.84,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-05-03","peak_price":87800,"drawdown_after_peak_pct":-56.66,"green_lateness_ratio":0.71,"four_b_local_peak_proximity":0.71,"four_b_full_window_peak_proximity":0.71,"four_b_timing_verdict":"late_green_near_full_window_peak","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"4B_overlay_success","current_profile_verdict":"current_profile_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L11_131290_20240426_79000","dedupe_for_aggregate":false,"aggregate_group_role":"label_comparison_only","is_new_independent_case":false,"reuse_reason":"same case late-Green comparison, not aggregate representative","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"trigger","trigger_id":"R2L11_T03_ISC_STAGE3_FALSE_GREEN_SOCKET_BLOWOFF","case_id":"R2L11_C08_095340_ISC_SOCKET_BLOWOFF","symbol":"095340","company_name":"ISC","round":"R2","loop":"11","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMI_TEST_SOCKET_HBM_NARRATIVE_BLOWOFF","sector":"AI·반도체·전자부품","primary_archetype":"semi test socket customer quality","loop_objective":"coverage_gap_fill|counterexample_mining|green_strictness_stress_test|yellow_threshold_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"Stage3-Green-FalsePositive","trigger_date":"2024-03-08","evidence_available_at_that_date":"HBM/test-socket narrative and sharp relative strength, but insufficient fresh customer mix/revision bridge; valuation/positioning risk dominated.","evidence_source":"public analyst/media summary; exact original URL enrichment required before production promotion","stage2_evidence_fields":["relative_strength","customer_or_order_quality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["valuation_blowoff","positioning_overheat","price_only_local_peak"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv","profile_path":"atlas/symbol_profiles/095/095340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-03-08","entry_price":95000,"MFE_30D_pct":13.68,"MFE_90D_pct":13.68,"MFE_180D_pct":13.68,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-12.63,"MAE_90D_pct":-38.21,"MAE_180D_pct":-56.74,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-03-28","peak_price":108000,"drawdown_after_peak_pct":-61.94,"green_lateness_ratio":0.31,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":[],"four_c_protection_label":"not_applicable","trigger_outcome_label":"false_positive_green","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L11_095340_20240308_95000","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"R2L11_T03B_ISC_4C_WATCH_AFTER_BLOWOFF","case_id":"R2L11_C08_095340_ISC_SOCKET_BLOWOFF","symbol":"095340","company_name":"ISC","round":"R2","loop":"11","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","fine_archetype_id":"SEMI_TEST_SOCKET_HBM_NARRATIVE_BLOWOFF","sector":"AI·반도체·전자부품","primary_archetype":"semi test socket customer quality","loop_objective":"coverage_gap_fill|counterexample_mining|green_strictness_stress_test|yellow_threshold_stress_test|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression","trigger_type":"4C-Watch","trigger_date":"2024-08-05","evidence_available_at_that_date":"Large price drawdown from the March peak; hard 4C would need non-price thesis break rather than price-only capitulation.","evidence_source":"public analyst/media summary; exact original URL enrichment required before production promotion","stage2_evidence_fields":[],"stage3_evidence_fields":[],"stage4b_evidence_fields":["positioning_overheat"],"stage4c_evidence_fields":["thesis_evidence_broken"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/095/095340/2024.csv","profile_path":"atlas/symbol_profiles/095/095340.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-08-05","entry_price":42550,"MFE_30D_pct":38.66,"MFE_90D_pct":41.36,"MFE_180D_pct":53.7,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":0.0,"MAE_90D_pct":0.0,"MAE_180D_pct":0.0,"MAE_1Y_pct":null,"below_entry_price_flag_30D":false,"below_entry_price_flag_90D":false,"peak_date":"2024-11-05","peak_price":65400,"drawdown_after_peak_pct":0.0,"green_lateness_ratio":0.31,"four_b_local_peak_proximity":null,"four_b_full_window_peak_proximity":null,"four_b_timing_verdict":"not_4B","four_b_evidence_type":[],"four_c_protection_label":"false_break_price_only_recovery","trigger_outcome_label":"4C_late_or_false_break","current_profile_verdict":"current_profile_4C_too_late","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R2L11_095340_20240805_42550","dedupe_for_aggregate":false,"aggregate_group_role":"4C_overlay_only","is_new_independent_case":false,"reuse_reason":"same case hard-4C protection stress test, not aggregate representative","independent_evidence_weight":0.25,"do_not_count_as_new_case":true}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L11_C08_058470_RINO_AI_TEST_SOCKET","trigger_id":"R2L11_T01_RINO_STAGE2_TEST_SOCKET_AI_EDGE_DEVICE","symbol":"058470","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":44,"relative_strength_score":62,"customer_quality_score":82,"policy_or_regulatory_score":0,"valuation_repricing_score":58,"execution_risk_score":25,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":0,"positioning_overheat_score":32,"thesis_break_score":0},"weighted_score_before":74.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":48,"relative_strength_score":68,"customer_quality_score":88,"policy_or_regulatory_score":0,"valuation_repricing_score":58,"execution_risk_score":24,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":0,"positioning_overheat_score":32,"thesis_break_score":0},"weighted_score_after":79.0,"stage_label_after":"Stage3-Yellow","changed_components":["customer_quality_score","relative_strength_score","revision_score"],"component_delta_explanation":"Repeatable test-socket franchise and relative strength justify Yellow, but late Green still needs fresh revision/customer confirmation.","MFE_90D_pct":47.85,"MAE_90D_pct":-10.1,"score_return_alignment_label":"Yellow aligned; Green too late near peak.","current_profile_verdict":"current_profile_too_late"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L11_C08_131290_TSE_HBM_PROBE_CARD","trigger_id":"R2L11_T02_TSE_STAGE2_HBM_PROBE_CARD_QUALITY","symbol":"131290","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":42,"relative_strength_score":65,"customer_quality_score":74,"policy_or_regulatory_score":0,"valuation_repricing_score":54,"execution_risk_score":38,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":0,"positioning_overheat_score":35,"thesis_break_score":0},"weighted_score_before":72.0,"stage_label_before":"Stage2-Actionable","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":47,"relative_strength_score":72,"customer_quality_score":79,"policy_or_regulatory_score":0,"valuation_repricing_score":54,"execution_risk_score":40,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":0,"positioning_overheat_score":37,"thesis_break_score":0},"weighted_score_after":77.0,"stage_label_after":"Stage3-Yellow","changed_components":["relative_strength_score","customer_quality_score","revision_score"],"component_delta_explanation":"Probe-card quality and relative strength justify Yellow, but high-MAE profile blocks automatic Green.","MFE_90D_pct":54.04,"MAE_90D_pct":-8.42,"score_return_alignment_label":"Stage2/Yellow aligned; 4B/Green timing needs guard.","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R2L11_C08_095340_ISC_SOCKET_BLOWOFF","trigger_id":"R2L11_T03_ISC_STAGE3_FALSE_GREEN_SOCKET_BLOWOFF","symbol":"095340","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","raw_component_scores_before":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":40,"relative_strength_score":78,"customer_quality_score":80,"policy_or_regulatory_score":0,"valuation_repricing_score":70,"execution_risk_score":45,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":0,"positioning_overheat_score":72,"thesis_break_score":0},"weighted_score_before":83.0,"stage_label_before":"Stage3-Green","raw_component_scores_after":{"contract_score":0,"backlog_visibility_score":0,"margin_bridge_score":0,"revision_score":34,"relative_strength_score":66,"customer_quality_score":68,"policy_or_regulatory_score":0,"valuation_repricing_score":48,"execution_risk_score":62,"legal_or_contract_risk_score":0,"dilution_cb_risk_score":0,"accounting_trust_risk_score":0,"capacity_or_shipment_score":0,"positioning_overheat_score":82,"thesis_break_score":0},"weighted_score_after":68.0,"stage_label_after":"Stage2-Watch","changed_components":["revision_score","customer_quality_score","valuation_repricing_score","execution_risk_score","positioning_overheat_score"],"component_delta_explanation":"Customer-quality narrative without fresh customer/revision bridge is capped; price-only HBM socket blowoff is not Green evidence.","MFE_90D_pct":13.68,"MAE_90D_pct":-38.21,"score_return_alignment_label":"After cap aligns with low MFE/high MAE counterexample.","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R2","loop":"11","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":3,"tested_existing_calibrated_axes":["stage2_actionable_evidence_bonus","stage3_yellow_total_min","stage3_green_total_min","stage3_green_revision_min","stage3_cross_evidence_green_buffer","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["price_only_socket_blowoff_false_green","late_green_after_most_upside_captured","high_MAE_success_needs_yellow_not_green","hard_4c_price_only_false_break_risk"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
{"row_type":"narrative_only","case_id":"R2L11_C08_095340_ISC_2023_PRE_CORP_ACTION_ROUTE","symbol":"095340","large_sector_id":"L2_AI_SEMICONDUCTOR_ELECTRONICS","canonical_archetype_id":"C08_SEMI_TEST_SOCKET_CUSTOMER_QUALITY","reason":"2023 ISC/SKC-related route was not used for quantitative calibration because the symbol profile has a 2023-10-20 corporate-action candidate; this loop uses 2024 post-event windows instead.","price_source":"Songdaiki/stock-web","usage":"not_weight_calibration"}
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
completed_round = R2
completed_loop = 11
next_round = R3
next_loop = 11
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- stock-web manifest: atlas/manifest.json
- 058470 profile: atlas/symbol_profiles/058/058470.json
- 131290 profile: atlas/symbol_profiles/131/131290.json
- 095340 profile: atlas/symbol_profiles/095/095340.json
- 058470 / 131290 / 095340 2024 OHLC rows: stock-web tradable shards listed in each trigger row.
- Evidence-source URLs require enrichment before production promotion.
- No live candidate scan, no production patch, no brokerage action.
