# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

| field | value |
|---|---|
| research_session | post_calibrated_sector_archetype_residual_research |
| mode | historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12 |
| output_file | e2r_stock_web_v12_residual_round_R1_loop_16_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY_research.md |
| scheduled_round | R1 |
| scheduled_loop | 16 |
| completed_round | R1 |
| completed_loop | 16 |
| large_sector_id | L1_INDUSTRIALS_INFRA_DEFENSE_GRID |
| canonical_archetype_id | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY |
| fine_archetype_id | NUCLEAR_POLICY_PROJECT_PREFERRED_BIDDER_EXECUTION_DELAY |
| production_scoring_changed | false |
| shadow_weight_only | true |
| handoff_prompt_embedded | true |
| handoff_prompt_executed_now | false |

This loop adds 3 new independent cases, 1 counterexamples, and 2 residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY.

## 1. Current Calibrated Profile Assumption

Current profile proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

Applied global axes assumed active:

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

This MD does not re-prove those axes. It stress-tests them inside C04 nuclear policy / project-delay cases.

## 2. Round / Large Sector / Canonical Archetype Scope

| item | value |
|---|---|
| scheduled_round | R1 |
| scheduled_loop | 16 |
| large_sector_id | L1_INDUSTRIALS_INFRA_DEFENSE_GRID |
| canonical_archetype_id | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY |
| round_sector_consistency | pass |
| selected reason | Previous local v12 schedule closed R13 Loop 15; next state is R1 Loop 16. R1 recent loops overused C02/C03, while C04 had no local v12 coverage. |
| loop_objective | coverage_gap_fill / sector_specific_rule_discovery / counterexample_mining / residual_false_positive_mining / 4B_non_price_requirement_stress_test / 4C_thesis_break_timing_test |

## 3. Previous Coverage / Duplicate Avoidance Check

Local v12 MD inventory in `/mnt/data` shows R1 Loop 10-15 were mostly C02/C03/C05. No local C04 v12 residual file was found. Therefore all three C04 cases here are treated as new independent cases.

| duplicate check | result |
|---|---|
| repeated canonical | allowed; C04 not previously materialized locally |
| repeated symbol + trigger_date + entry_date | no previous C04 local row found |
| minimum_new_symbol_count | pass: 3 |
| minimum_counterexample_count | pass: 1 |
| minimum_positive_case_count | pass: 2 including one high-MAE success |
| new_independent_case_ratio | 3/3 = 1.00 |

## 4. Stock-Web OHLC Input / Price Source Validation

| manifest field | value |
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

Schema notes: tradable shards use `d,o,h,l,c,v,a,mc,s,m`; MFE/MAE are computed from maximum high and minimum low over N tradable rows; calibration requires entry row, 180 forward tradable rows, positive OHLC/volume, and no blocked corporate-action window.

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | 180D available by manifest max_date | corporate action 180D window | calibration_usable |
|---|---:|---:|---:|---|---|
| R1L16_C04_034020_CZECH_PREF_HIGH_MAE | 034020 | 2024-07-18 | yes | clean_180D_window; profile CA candidates are 2019-05-29, 2020-02-18, 2020-12-24 | true |
| R1L16_C04_051600_CZECH_PREF_OM_BRIDGE | 051600 | 2024-07-18 | yes | clean_180D_window; profile has no CA candidates | true |
| R1L16_C04_052690_CZECH_PREF_DESIGN_PROXY_FALSE_GREEN | 052690 | 2024-07-18 | yes | clean_180D_window; profile has no CA candidates | true |

## 6. Canonical Archetype Compression Map

C04 is not simply "nuclear policy is good." It is a three-step bridge:

```text
policy / preferred bidder evidence
→ signed contract / consortium role / revenue bridge
→ margin and revision confirmation
```

The loop compresses three fine patterns into one canonical shadow rule:

| fine pattern | canonical mapping | scoring implication |
|---|---|---|
| preferred bidder with no final signed contract | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | cap Green; allow Stage2-Actionable only |
| O&M/service revenue bridge | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | eligible for higher Stage2/Yellow score due to lower MAE |
| design/EPC proxy blowoff | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | block Green unless revision/margin bridge exists |

## 7. Case Selection Summary

| case_id | symbol | company | role | trigger_date | entry_date | entry_price | outcome |
|---|---:|---|---|---:|---:|---:|---|
| R1L16_C04_034020_CZECH_PREF_HIGH_MAE | 034020 | 두산에너빌리티 | high_mae_success | 2024-07-17 | 2024-07-18 | 21000 | positive but current profile too early |
| R1L16_C04_051600_CZECH_PREF_OM_BRIDGE | 051600 | 한전KPS | structural_success | 2024-07-17 | 2024-07-18 | 38900 | positive lower drawdown |
| R1L16_C04_052690_CZECH_PREF_DESIGN_PROXY_FALSE_GREEN | 052690 | 한전기술 | false_positive_green | 2024-07-17 | 2024-07-18 | 82000 | counterexample / same-day peak |

## 8. Positive vs Counterexample Balance

| bucket | count | cases |
|---|---:|---|
| positive structural / lower-MAE success | 1 | 051600 |
| high-MAE success | 1 | 034020 |
| counterexample / false Green | 1 | 052690 |
| 4B/4C overlay evidence | 3 | all cases have price-only 4B or legal-delay watch labels |

## 9. Evidence Source Map

| evidence family | evidence date | source note |
|---|---:|---|
| KHNP selected as Czech preferred bidder | 2024-07-17 | Reuters reported KHNP was selected by the Czech government as preferred bidder for two Dukovany reactors; final contract terms remained to be agreed later. |
| stock reaction | 2024-07-18 | Stock-web rows show same/next trading-day gaps and high-volume moves across 034020, 051600, 052690. |
| appeal / legal-delay route | 2024-10-30 and 2025-05-06 | Reuters and AP later reported Czech watchdog/court blocks or pauses related to appeals, validating that C04 needs legal/project-delay guardrails. |

## 10. Price Data Source Map

| symbol | company | tradable shard(s) used | profile |
|---:|---|---|---|
| 034020 | 두산에너빌리티 | `atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv`, `2025.csv` | `atlas/symbol_profiles/034/034020.json` |
| 051600 | 한전KPS | `atlas/ohlcv_tradable_by_symbol_year/051/051600/2024.csv`, `2025.csv` | `atlas/symbol_profiles/051/051600.json` |
| 052690 | 한전기술 | `atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv`, `2025.csv` | `atlas/symbol_profiles/052/052690.json` |

## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | trigger_type | Stage2 evidence | Stage3 evidence | 4B evidence | 4C evidence | current verdict |
|---|---|---|---|---|---|---|---|
| TRG_R1L16_C04_034020_CZECH_PREF_HIGH_MAE | R1L16_C04_034020_CZECH_PREF_HIGH_MAE | Stage2-Actionable | public event, policy optionality, customer/order quality | multiple public sources only | price-only local peak, positioning | legal/regulatory block watch | current_profile_too_early |
| TRG_R1L16_C04_051600_CZECH_PREF_OM_BRIDGE | R1L16_C04_051600_CZECH_PREF_OM_BRIDGE | Stage2-Actionable | public event, policy optionality, customer/order quality | public sources, financial visibility, lower red-team risk | valuation blowoff watch | legal/regulatory block watch | current_profile_correct |
| TRG_R1L16_C04_052690_CZECH_PREF_DESIGN_PROXY_FALSE_GREEN | R1L16_C04_052690_CZECH_PREF_DESIGN_PROXY_FALSE_GREEN | Stage2-Actionable | public event, policy optionality, relative strength | multiple public sources only | same-day price-only peak, valuation blowoff | legal/regulatory block watch | current_profile_false_positive |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_date | entry_price | MFE_30D_pct | MAE_30D_pct | MFE_90D_pct | MAE_90D_pct | MFE_180D_pct | MAE_180D_pct | peak_date | peak_price | drawdown_after_peak_pct |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 034020 | 2024-07-18 | 21000 | 19.05 | -27.86 | 19.05 | -27.86 | 47.14 | -27.86 | 2025-02-19 | 30900 | -50.97 |
| 051600 | 2024-07-18 | 38900 | 21.98 | -7.84 | 24.04 | -7.84 | 26.22 | -7.84 | 2024-12-03 | 49100 | -26.99 |
| 052690 | 2024-07-18 | 82000 | 19.63 | -24.88 | 19.63 | -24.88 | 19.63 | -39.94 | 2024-07-18 | 98100 | -49.80 |

Raw row anchors:

```text
034020: 2024-07-18 c=21000 h=25000; 2024-08-05 l=15150; 2025-02-19 h=30900.
051600: 2024-07-18 c=38900 h=47450; 2024-08-05 l=35850; 2024-11-27 h=48250; 2024-12-03 h=49100.
052690: 2024-07-18 c=82000 h=98100; 2024-08-05 l=61600; 2024-12-10 l=49250.
```

## 13. Current Calibrated Profile Stress Test

| case | expected current-profile action | actual MFE/MAE alignment | verdict |
|---|---|---|---|
| 034020 | Stage3-Yellow possible due to policy + order optionality | 180D MFE good but 30/90D MAE is too large for clean Green | current_profile_too_early |
| 051600 | Stage3-Yellow / Stage2-Actionable | 90D and 180D MFE positive with low MAE | current_profile_correct |
| 052690 | Stage3-Yellow/Green-risk possible if relative strength overweighted | same-day peak; 180D MAE -39.94% | current_profile_false_positive |

Answers to required checks:

```text
1. Current profile would likely treat all three as Stage2-Actionable or Yellow; 052690 might approach Green due to relative strength.
2. 051600 aligns. 034020 aligns only after tolerating high MAE. 052690 does not align.
3. Stage2 bonus is useful for 051600, too permissive for 052690 if relative strength dominates.
4. Yellow threshold 75 is acceptable, but C04 needs evidence-family caps.
5. Green 87 / revision 55 should remain strict; C04 should not Green without signed contract or revision bridge.
6. Price-only blowoff guard is strongly appropriate for 052690.
7. Full 4B non-price requirement remains appropriate; price-only local peaks should be overlay only.
8. Hard 4C routing should activate on legal/project block evidence, but not retroactively train positive entry weights.
```

## 14. Stage2 / Yellow / Green Comparison

C04 differs from C02/C03 because a preferred bidder is not the same thing as a signed, executable, revenue-recognizable contract. The correct stage ladder is:

```text
Stage2-Actionable: preferred bidder / policy optionality / credible consortium role
Stage3-Yellow: preferred bidder + specific role + revenue bridge visibility
Stage3-Green: signed contract + revision/margin bridge + low legal/project block risk
4B overlay: price-only spike, valuation blowoff, appeal risk, contract delay
4C: explicit contract block/cancel/legal thesis break
```

Green lateness ratio is not applicable because no confirmed Stage3-Green trigger was used. This loop is a Green-strictness stress test, not an entry-timing optimization.

## 15. 4B Local vs Full-window Timing Audit

| symbol | 4B evidence | local peak proximity | full-window peak proximity | verdict |
|---:|---|---:|---:|---|
| 034020 | price-only / positioning | 0.43 | 0.35 | price-only local 4B too early; not full 4B |
| 051600 | valuation watch only | 0.84 | 0.93 | no full 4B until non-price slowdown |
| 052690 | price-only peak + valuation blowoff | 1.00 | 1.00 | same-day full-window peak; strong 4B overlay |

## 16. 4C Protection Audit

| symbol | 4C evidence type | label | interpretation |
|---:|---|---|---|
| 034020 | later legal/project delay watch | thesis_break_watch_only | Do not train positive weights from later legal overhang; use as risk overlay. |
| 051600 | later legal/project delay watch | thesis_break_watch_only | Legal delay did not destroy the 180D setup, but should cap late Green. |
| 052690 | appeal / contract finalization risk | hard_4c_late_watch | Price peaked before explicit legal block; a C04-specific pre-4C watch is needed. |

## 17. Sector-Specific Rule Candidate

`sector_specific_rule_candidate = true`

R1 nuclear/project-delay names should not inherit the same Green treatment as direct backlog or defense framework contracts. A preferred-bidder event is closer to a **reservation ticket** than a delivered order: it opens the gate, but it does not move margin into the house yet.

Candidate rule:

```text
In L1/C04, preferred-bidder evidence can promote Stage2-Actionable.
It can support Stage3-Yellow only when role-specific revenue bridge is visible.
It cannot support Stage3-Green unless signed-contract, margin/revision, and low legal block risk are also present.
```

## 18. Canonical-Archetype Rule Candidate

`canonical_archetype_rule_candidate = true`

Proposed C04 shadow axes:

```text
c04_preferred_bidder_without_signed_contract_green_cap = true
c04_om_service_revenue_bridge_bonus = +1
c04_design_epc_proxy_blowoff_penalty = +1 risk overlay
c04_legal_project_delay_pre_4c_watch = true
```

## 19. Before / After Backtest Comparison

| profile_id | eligible_trigger_count | selected cases | avg_MFE_90D_pct | avg_MAE_90D_pct | avg_MFE_180D_pct | avg_MAE_180D_pct | false_positive_rate | missed_structural_count | score_return_alignment_verdict |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | all | 20.91 | -20.19 | 31.0 | -25.21 | 0.33 | 0 | mixed; false positive remains |
| P0b e2r_2_0_baseline_reference | 3 | all, looser Green risk | 20.91 | -20.19 | 31.0 | -25.21 | 0.33 | 0 | too permissive for 052690 |
| P1 sector_specific_candidate_profile | 2 | 051600, 034020 watch | 21.55 | -17.85 | 36.68 | -17.85 | 0.00 | 0 | better but 034020 high-MAE remains |
| P2 canonical_archetype_candidate_profile | 2 | 051600 + cautious 034020 | 21.55 | -17.85 | 36.68 | -17.85 | 0.00 | 0 | best explanatory balance |
| P3 counterexample_guard_profile | 1 | 051600 only | 24.04 | -7.84 | 26.22 | -7.84 | 0.00 | 1 | safest but may miss high-MAE recovery |

## 20. Score-Return Alignment Matrix

| symbol | weighted_before | stage_before | weighted_after | stage_after | MFE_90D | MAE_90D | alignment |
|---:|---:|---|---:|---|---:|---:|---|
| 034020 | 78.0 | Stage3-Yellow | 72.0 | Stage2-Actionable | 19.05 | -27.86 | high-MAE success; do not Green |
| 051600 | 80.0 | Stage3-Yellow | 83.0 | Stage3-Yellow | 24.04 | -7.84 | aligned positive |
| 052690 | 81.0 | Stage3-Yellow/Green-risk | 68.0 | Stage2-Actionable / 4B-watch | 19.63 | -24.88 | false Green blocked |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY | NUCLEAR_POLICY_PROJECT_PREFERRED_BIDDER_EXECUTION_DELAY | 2 | 1 | 3 | 3 watch-only | 3 | 0 | 3 | 3 | 2 | true | true | C04 now has initial positive/counterexample coverage; needs future signed-contract and cancellation rows |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 1
tested_existing_calibrated_axes:
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - preferred_bidder_event_false_green
  - same_day_price_blowoff
  - policy_event_high_mae_success
  - signed_contract_delay_risk
new_axis_proposed:
  - c04_preferred_bidder_without_signed_contract_green_cap
  - c04_om_service_revenue_bridge_bonus
  - c04_design_epc_proxy_blowoff_penalty
  - c04_legal_project_delay_pre_4c_watch
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_total_min
  - stage3_green_revision_min
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

```text
- 2024-07-18 entry rows exist in stock-web tradable shards.
- 180D forward windows are available before manifest max_date 2026-02-20.
- 30D/90D/180D MFE/MAE were calculated from observed high/low anchors.
- Corporate-action contaminated windows were not present in 180D windows for selected cases.
- C04 preferred-bidder events need a signed-contract/revenue-bridge gate before Green.
```

Not validated:

```text
- No current/live candidate search.
- No production scoring patch.
- No brokerage API or auto-trading.
- No claim that these symbols are current buy/sell candidates.
- No 1Y/2Y quantitative calibration in this loop; 2Y is unavailable for 2024-07 entries by manifest max_date.
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c04_preferred_bidder_without_signed_contract_green_cap,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY,0,1,+1,"Preferred bidder without signed contract caused 052690 false Green and 034020 high-MAE entry.","Blocks Green until signed contract / revision bridge.",TRG_R1L16_C04_034020_CZECH_PREF_HIGH_MAE|TRG_R1L16_C04_052690_CZECH_PREF_DESIGN_PROXY_FALSE_GREEN,3,3,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c04_om_service_revenue_bridge_bonus,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY,0,1,+1,"051600 O&M/service bridge had lower MAE and better score-return alignment.","Allows Yellow but not automatic Green.",TRG_R1L16_C04_051600_CZECH_PREF_OM_BRIDGE,3,3,1,low,canonical_shadow_only,"needs more O&M examples"
shadow_weight,c04_design_epc_proxy_blowoff_penalty,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY,0,1,+1,"052690 peaked on event day and produced -39.94% 180D MAE.","Demotes design/EPC proxy with no signed-contract/revision bridge.",TRG_R1L16_C04_052690_CZECH_PREF_DESIGN_PROXY_FALSE_GREEN,3,3,1,medium,canonical_shadow_only,"not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type":"price_source_validation","source":"Songdaiki/stock-web","source_url":"https://github.com/Songdaiki/stock-web","manifest_path":"atlas/manifest.json","schema_path":"atlas/schema.json","universe_path":"atlas/universe/all_symbols.csv","manifest_max_date":"2026-02-20","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","calibration_shard_root":"atlas/ohlcv_tradable_by_symbol_year","raw_shard_root":"atlas/ohlcv_raw_by_symbol_year","validation_status":"usable_for_historical_calibration"}
{"row_type":"case","case_id":"R1L16_C04_034020_CZECH_PREF_HIGH_MAE","symbol":"034020","company_name":"두산에너빌리티","round":"R1","loop":"16","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_POLICY_PROJECT_PREFERRED_BIDDER_EXECUTION_DELAY","case_type":"high_mae_success","positive_or_counterexample":"positive_with_high_mae","best_trigger":"TRG_R1L16_C04_034020_CZECH_PREF_HIGH_MAE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"high_mae_success_after_policy_event","current_profile_verdict":"current_profile_too_early","price_source":"Songdaiki/stock-web","notes":"정책·우선협상자 이벤트 자체는 맞았지만, entry 직후 30D/90D MAE가 -27.86%로 컸다. Green이 아니라 Stage2-Actionable/Yellow-watch로 다루는 쪽이 더 설명력이 높다."}
{"row_type":"case","case_id":"R1L16_C04_051600_CZECH_PREF_OM_BRIDGE","symbol":"051600","company_name":"한전KPS","round":"R1","loop":"16","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_POLICY_PROJECT_PREFERRED_BIDDER_EXECUTION_DELAY","case_type":"structural_success","positive_or_counterexample":"positive","best_trigger":"TRG_R1L16_C04_051600_CZECH_PREF_OM_BRIDGE","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"structural_success_lower_drawdown_service_bridge","current_profile_verdict":"current_profile_correct","price_source":"Songdaiki/stock-web","notes":"정비·운영 서비스 성격의 revenue bridge가 EPC/설계 proxy보다 drawdown이 낮았다. 같은 원전 정책 이벤트라도 C04 안에서 service/O&M bridge를 별도 가산하는 근거."}
{"row_type":"case","case_id":"R1L16_C04_052690_CZECH_PREF_DESIGN_PROXY_FALSE_GREEN","symbol":"052690","company_name":"한전기술","round":"R1","loop":"16","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_POLICY_PROJECT_PREFERRED_BIDDER_EXECUTION_DELAY","case_type":"false_positive_green","positive_or_counterexample":"counterexample","best_trigger":"TRG_R1L16_C04_052690_CZECH_PREF_DESIGN_PROXY_FALSE_GREEN","calibration_usable":true,"is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"score_price_alignment":"same_day_price_blowoff_then_legal_execution_drag","current_profile_verdict":"current_profile_false_positive","price_source":"Songdaiki/stock-web","notes":"설계/엔지니어링 proxy는 이벤트 당일 고점이 full-window peak였다. 수주 계약·마진·revision 확인 전 Green 승격은 가격-only blowoff와 사실상 구분되지 않는다."}
{"row_type":"trigger","trigger_id":"TRG_R1L16_C04_034020_CZECH_PREF_HIGH_MAE","case_id":"R1L16_C04_034020_CZECH_PREF_HIGH_MAE","symbol":"034020","company_name":"두산에너빌리티","round":"R1","loop":"16","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_POLICY_PROJECT_PREFERRED_BIDDER_EXECUTION_DELAY","sector":"산업재·인프라·방산·전력망","primary_archetype":"nuclear preferred bidder policy optionality vs signed-contract revenue bridge","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-17","evidence_available_at_that_date":"Czech government selected KHNP as preferred bidder for Dukovany nuclear reactors; Korean nuclear supply chain stocks reacted immediately, but final contract/appeal risks remained unresolved.","evidence_source":"Reuters 2024-07-17; Reuters 2024-10-30 follow-up on Czech watchdog appeals; AP 2025-05-06 court block note.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","customer_or_order_quality"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["price_only_local_peak","positioning_overheat"],"stage4c_evidence_fields":["legal_or_regulatory_block"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/034/034020/2024.csv","profile_path":"atlas/symbol_profiles/034/034020.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-18","entry_price":21000.0,"MFE_30D_pct":19.05,"MFE_90D_pct":19.05,"MFE_180D_pct":47.14,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-27.86,"MAE_90D_pct":-27.86,"MAE_180D_pct":-27.86,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2025-02-19","peak_price":30900.0,"drawdown_after_peak_pct":-50.97,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.43,"four_b_full_window_peak_proximity":0.35,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"high_mae_success_after_policy_event","current_profile_verdict":"current_profile_too_early","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L16_C04_034020_CZECH_PREF_HIGH_MAE_2024-07-18","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R1L16_C04_051600_CZECH_PREF_OM_BRIDGE","case_id":"R1L16_C04_051600_CZECH_PREF_OM_BRIDGE","symbol":"051600","company_name":"한전KPS","round":"R1","loop":"16","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_POLICY_PROJECT_PREFERRED_BIDDER_EXECUTION_DELAY","sector":"산업재·인프라·방산·전력망","primary_archetype":"nuclear preferred bidder policy optionality vs signed-contract revenue bridge","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-17","evidence_available_at_that_date":"KHNP preferred-bidder event improved perceived long-cycle maintenance and O&M optionality; stock-web 180D path showed MFE with much smaller MAE than EPC/design proxy.","evidence_source":"Reuters 2024-07-17; stock-web OHLC rows 2024-07-18 through 2025-04-14.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","customer_or_order_quality"],"stage3_evidence_fields":["multiple_public_sources","financial_visibility","low_red_team_risk"],"stage4b_evidence_fields":["valuation_blowoff"],"stage4c_evidence_fields":["legal_or_regulatory_block"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/051/051600/2024.csv","profile_path":"atlas/symbol_profiles/051/051600.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-18","entry_price":38900.0,"MFE_30D_pct":21.98,"MFE_90D_pct":24.04,"MFE_180D_pct":26.22,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-7.84,"MAE_90D_pct":-7.84,"MAE_180D_pct":-7.84,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-12-03","peak_price":49100.0,"drawdown_after_peak_pct":-26.99,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":0.84,"four_b_full_window_peak_proximity":0.93,"four_b_timing_verdict":"no_full_4B_until_non_price_evidence","four_b_evidence_type":["valuation_blowoff"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"structural_success_lower_drawdown_service_bridge","current_profile_verdict":"current_profile_correct","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L16_C04_051600_CZECH_PREF_OM_BRIDGE_2024-07-18","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"trigger","trigger_id":"TRG_R1L16_C04_052690_CZECH_PREF_DESIGN_PROXY_FALSE_GREEN","case_id":"R1L16_C04_052690_CZECH_PREF_DESIGN_PROXY_FALSE_GREEN","symbol":"052690","company_name":"한전기술","round":"R1","loop":"16","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","fine_archetype_id":"NUCLEAR_POLICY_PROJECT_PREFERRED_BIDDER_EXECUTION_DELAY","sector":"산업재·인프라·방산·전력망","primary_archetype":"nuclear preferred bidder policy optionality vs signed-contract revenue bridge","loop_objective":"coverage_gap_fill|sector_specific_rule_discovery|counterexample_mining|residual_false_positive_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test","trigger_type":"Stage2-Actionable","trigger_date":"2024-07-17","evidence_available_at_that_date":"Preferred-bidder news created immediate spike, but contract-finalization/legal-overhang risk later became material; price path peaked on entry day and suffered deep 180D MAE.","evidence_source":"Reuters 2024-07-17; Reuters 2024-10-30; AP 2025-05-06.","stage2_evidence_fields":["public_event_or_disclosure","policy_or_regulatory_optionality","relative_strength"],"stage3_evidence_fields":["multiple_public_sources"],"stage4b_evidence_fields":["price_only_local_peak","valuation_blowoff","positioning_overheat"],"stage4c_evidence_fields":["legal_or_regulatory_block"],"price_data_source":"Songdaiki/stock-web","price_data_repo":"https://github.com/Songdaiki/stock-web","price_shard_path":"atlas/ohlcv_tradable_by_symbol_year/052/052690/2024.csv","profile_path":"atlas/symbol_profiles/052/052690.json","price_basis":"tradable_raw","price_adjustment_status":"raw_unadjusted_marcap","stock_web_manifest_max_date":"2026-02-20","entry_date":"2024-07-18","entry_price":82000.0,"MFE_30D_pct":19.63,"MFE_90D_pct":19.63,"MFE_180D_pct":19.63,"MFE_1Y_pct":null,"MFE_2Y_pct":null,"MAE_30D_pct":-24.88,"MAE_90D_pct":-24.88,"MAE_180D_pct":-39.94,"MAE_1Y_pct":null,"below_entry_price_flag_30D":true,"below_entry_price_flag_90D":true,"peak_date":"2024-07-18","peak_price":98100.0,"drawdown_after_peak_pct":-49.8,"green_lateness_ratio":"not_applicable","four_b_local_peak_proximity":1.0,"four_b_full_window_peak_proximity":1.0,"four_b_timing_verdict":"price_only_local_4B_too_early","four_b_evidence_type":["price_only","valuation_blowoff","positioning_overheat"],"four_c_protection_label":"thesis_break_watch_only","trigger_outcome_label":"same_day_price_blowoff_then_legal_execution_drag","current_profile_verdict":"current_profile_false_positive","calibration_usable":true,"forward_window_trading_days":180,"calibration_block_reasons":[],"corporate_action_window_status":"clean_180D_window","same_entry_group_id":"R1L16_C04_052690_CZECH_PREF_DESIGN_PROXY_FALSE_GREEN_2024-07-18","dedupe_for_aggregate":true,"aggregate_group_role":"representative","is_new_independent_case":true,"reuse_reason":null,"independent_evidence_weight":1.0,"do_not_count_as_new_case":false}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L16_C04_034020_CZECH_PREF_HIGH_MAE","trigger_id":"TRG_R1L16_C04_034020_CZECH_PREF_HIGH_MAE","symbol":"034020","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","raw_component_scores_before":{"contract_score":40,"backlog_visibility_score":45,"margin_bridge_score":25,"revision_score":25,"relative_strength_score":50,"customer_quality_score":45,"policy_or_regulatory_score":80,"valuation_repricing_score":45,"execution_risk_score":55,"legal_or_contract_risk_score":35,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_before":78.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":40,"backlog_visibility_score":45,"margin_bridge_score":25,"revision_score":25,"relative_strength_score":45,"customer_quality_score":45,"policy_or_regulatory_score":75,"valuation_repricing_score":40,"execution_risk_score":60,"legal_or_contract_risk_score":45,"dilution_cb_risk_score":10,"accounting_trust_risk_score":10},"weighted_score_after":72.0,"stage_label_after":"Stage2-Actionable","changed_components":["relative_strength_score","policy_or_regulatory_score","legal_or_contract_risk_score","execution_risk_score","margin_bridge_score"],"component_delta_explanation":"C04 shadow profile caps Green when preferred-bidder evidence is not yet signed-contract/revenue-bridge evidence; O&M/service bridge gets more credit than design/EPC proxy.","MFE_90D_pct":19.05,"MAE_90D_pct":-27.86,"score_return_alignment_label":"high_mae_success_after_policy_event","current_profile_verdict":"current_profile_too_early"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L16_C04_051600_CZECH_PREF_OM_BRIDGE","trigger_id":"TRG_R1L16_C04_051600_CZECH_PREF_OM_BRIDGE","symbol":"051600","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","raw_component_scores_before":{"contract_score":55,"backlog_visibility_score":55,"margin_bridge_score":45,"revision_score":45,"relative_strength_score":55,"customer_quality_score":55,"policy_or_regulatory_score":75,"valuation_repricing_score":45,"execution_risk_score":25,"legal_or_contract_risk_score":25,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":80.0,"stage_label_before":"Stage3-Yellow","raw_component_scores_after":{"contract_score":60,"backlog_visibility_score":60,"margin_bridge_score":50,"revision_score":45,"relative_strength_score":55,"customer_quality_score":60,"policy_or_regulatory_score":75,"valuation_repricing_score":45,"execution_risk_score":25,"legal_or_contract_risk_score":30,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":83.0,"stage_label_after":"Stage3-Yellow","changed_components":["relative_strength_score","policy_or_regulatory_score","legal_or_contract_risk_score","execution_risk_score","margin_bridge_score"],"component_delta_explanation":"C04 shadow profile caps Green when preferred-bidder evidence is not yet signed-contract/revenue-bridge evidence; O&M/service bridge gets more credit than design/EPC proxy.","MFE_90D_pct":24.04,"MAE_90D_pct":-7.84,"score_return_alignment_label":"structural_success_lower_drawdown_service_bridge","current_profile_verdict":"current_profile_correct"}
{"row_type":"score_simulation","profile_id":"e2r_2_1_stock_web_calibrated_proxy","case_id":"R1L16_C04_052690_CZECH_PREF_DESIGN_PROXY_FALSE_GREEN","trigger_id":"TRG_R1L16_C04_052690_CZECH_PREF_DESIGN_PROXY_FALSE_GREEN","symbol":"052690","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","raw_component_scores_before":{"contract_score":35,"backlog_visibility_score":30,"margin_bridge_score":15,"revision_score":20,"relative_strength_score":80,"customer_quality_score":45,"policy_or_regulatory_score":80,"valuation_repricing_score":70,"execution_risk_score":55,"legal_or_contract_risk_score":40,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_before":81.0,"stage_label_before":"Stage3-Yellow/Green-risk","raw_component_scores_after":{"contract_score":30,"backlog_visibility_score":25,"margin_bridge_score":15,"revision_score":20,"relative_strength_score":55,"customer_quality_score":40,"policy_or_regulatory_score":70,"valuation_repricing_score":55,"execution_risk_score":70,"legal_or_contract_risk_score":60,"dilution_cb_risk_score":0,"accounting_trust_risk_score":5},"weighted_score_after":68.0,"stage_label_after":"Stage2-Actionable / 4B-watch","changed_components":["relative_strength_score","policy_or_regulatory_score","legal_or_contract_risk_score","execution_risk_score","margin_bridge_score"],"component_delta_explanation":"C04 shadow profile caps Green when preferred-bidder evidence is not yet signed-contract/revenue-bridge evidence; O&M/service bridge gets more credit than design/EPC proxy.","MFE_90D_pct":19.63,"MAE_90D_pct":-24.88,"score_return_alignment_label":"same_day_price_blowoff_then_legal_execution_drag","current_profile_verdict":"current_profile_false_positive"}
{"row_type":"residual_contribution","round":"R1","loop":"16","large_sector_id":"L1_INDUSTRIALS_INFRA_DEFENSE_GRID","canonical_archetype_id":"C04_NUCLEAR_POLICY_PROJECT_LEGAL_DELAY","new_independent_case_count":3,"reused_case_count":0,"new_symbol_count":3,"new_trigger_family_count":1,"tested_existing_calibrated_axes":["stage3_green_total_min","stage3_green_revision_min","price_only_blowoff_blocks_positive_stage","full_4b_requires_non_price_evidence","hard_4c_thesis_break_routes_to_4c"],"residual_error_types_found":["preferred_bidder_event_false_green","same_day_price_blowoff","policy_event_high_mae_success","signed_contract_delay_risk"],"loop_contribution_label":"canonical_archetype_rule_candidate","do_not_propose_new_weight_delta":false}
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
completed_round = R1
completed_loop = 16
next_round = R2
next_loop = 16
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
price_atlas_repo = https://github.com/Songdaiki/stock-web
manifest = atlas/manifest.json
schema = atlas/schema.json
profile_paths =
  - atlas/symbol_profiles/034/034020.json
  - atlas/symbol_profiles/051/051600.json
  - atlas/symbol_profiles/052/052690.json
evidence_sources =
  - Reuters, 2024-07-17, Czech government selected KHNP as preferred bidder for Dukovany nuclear reactors.
  - Reuters, 2024-10-30, Czech watchdog temporarily prohibited finalization amid appeals.
  - AP, 2025-05-06, Czech court temporarily blocked KHNP deal signing.
```

