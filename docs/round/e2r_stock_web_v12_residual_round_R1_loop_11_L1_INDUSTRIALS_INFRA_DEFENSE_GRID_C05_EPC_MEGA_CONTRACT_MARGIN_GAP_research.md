# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
scheduled_round: R1
scheduled_loop: 11
completed_round: R1
completed_loop: 11
large_sector_id: L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id: C05_EPC_MEGA_CONTRACT_MARGIN_GAP
fine_archetype_id: EPC_MEGA_CONTRACT_BACKLOG_MARGIN_CONVERSION_GUARD
output_file: e2r_stock_web_v12_residual_round_R1_loop_11_L1_INDUSTRIALS_INFRA_DEFENSE_GRID_C05_EPC_MEGA_CONTRACT_MARGIN_GAP_research.md
production_scoring_changed: false
shadow_weight_only: true
stock_agent_code_access_allowed: false
stock_agent_code_patch_allowed: false
stock_web_price_atlas_access_required: true
```

This loop adds **5** new independent cases, **3** counterexamples, and **4** residual errors for `R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C05_EPC_MEGA_CONTRACT_MARGIN_GAP`.

## 1. Current Calibrated Profile Assumption

`P0 = e2r_2_1_stock_web_calibrated_proxy`.

Already-applied global axes are treated as existing infrastructure, not new discoveries:

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

The research question here is narrower: **when does an EPC mega-contract or backlog headline become an earnings/margin conversion signal, and when is it only an orderbook story that should be capped before Stage3-Green?**

## 2. Round / Large Sector / Canonical Archetype Scope

| field | value |
|---|---|
| scheduled_round | R1 |
| scheduled_loop | 11 |
| large_sector_id | L1_INDUSTRIALS_INFRA_DEFENSE_GRID |
| canonical_archetype_id | C05_EPC_MEGA_CONTRACT_MARGIN_GAP |
| fine_archetype_id | EPC_MEGA_CONTRACT_BACKLOG_MARGIN_CONVERSION_GUARD |
| loop_objective | coverage_gap_fill; counterexample_mining; sector_specific_rule_discovery; green_strictness_stress_test; 4C_thesis_break_timing_test |
| round_schedule_status | valid |
| round_sector_consistency | pass |

R1 maps to `L1_INDUSTRIALS_INFRA_DEFENSE_GRID`; C05 is treated as the EPC/mega-contract branch of industrial infrastructure rather than the R10 PF/balance-sheet branch.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed artifact reviewed: `reports/e2r_calibration/by_round/R1.md`.

R1 already contains representative triggers and cumulative applied axes. This loop therefore avoids re-proving the Stage2 bonus or generic Green lateness. It fills the C05 gap by separating:

1. EPC/orderbook headline with margin bridge,
2. overseas backlog quality but no clean margin conversion,
3. orderbook or valuation rerating without realized margin,
4. legal/quality break that should override contract/backlog interpretation.

Reused symbols are permitted only where the trigger family changes from R10 PF/balance-sheet risk to R1/C05 EPC margin conversion. They carry partial independent evidence weight.

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

Price basis: `tradable_raw`. Adjustment status: `raw_unadjusted_marcap`. MFE/MAE are rounded from stock-web tradable shard rows or prior loop rows that were already calculated from the same stock-web shards and explicitly re-scoped here.

## 5. Historical Eligibility Gate

| gate | status |
|---|---|
| all trigger dates are historical | pass |
| entry rows exist in tradable shards | pass |
| forward 180 trading days available by manifest max_date | pass |
| positive OHLCV fields present | pass |
| 30D/90D/180D MFE/MAE computed | pass |
| corporate action contamination in selected 180D windows | none detected from selected symbol profiles |
| calibration_usable_case_count | 5 |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | included fine_archetypes | compression rule |
|---|---|---|
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | EPC_MEGA_CONTRACT_BACKLOG_MARGIN_CONVERSION; OVERSEAS_EPC_ORDERBOOK_QUALITY; VALUATION_BACKLOG_FALSE_GREEN; QUALITY_LEGAL_HARD_4C_OVERRIDE | compress EPC/mega-contract cases into C05, but split contract/backlog headline from realized margin/revision bridge and quality/legal thesis breaks |

## 7. Case Selection Summary

| case_id | symbol | role | trigger_family | why selected | new? | reuse |
|---|---:|---|---|---|---|---|
| `R1L11_C05_SAMSUNGEA_MARGIN_BRIDGE_20240131` | `028050` | positive / structural_success | EPC margin bridge after order/earnings reset | EPC headline alone had been noisy, but low entry after earnings reset created a clean test of backlog-to-margin bridge instead of pure orderbook excitement. | true |  |
| `R1L11_C05_HYUNDAIENG_OVERSEAS_EPC_20240125` | `000720` | positive / stage2_promote_candidate | overseas EPC backlog quality with domestic PF drag | Same symbol appeared in R10 for PF guard, but this row reuses it only for a different C05 trigger family: overseas EPC backlog quality versus margin conversion. | true | same symbol was used in R10 C30, but C05 uses a new overseas EPC backlog/margin trigger family; count with partial independent weight. |
| `R1L11_C05_DAEWOOENG_ORDERBOOK_MARGIN_GAP_20240131` | `047040` | counterexample / failed_rerating | orderbook headline without realized margin bridge | Adds a new C05 symbol where orderbook/backlog optics did not convert into clean 90D/180D price reward. | true |  |
| `R1L11_C05_DLEC_VALUATION_CONTRACT_GAP_20240110` | `375500` | counterexample / false_positive_green | valuation/orderbook bounce without EPC margin bridge | Reused from R10 only as new C05 margin-gap counterexample; the same price row now tests EPC/contract conversion, not PF-balance-sheet survival. | true | same symbol/entry appears in R10 C30, but this loop reuses it for a C05 EPC margin-gap failure mode with partial independent weight. |
| `R1L11_C05_GSENG_QUALITY_4C_20230706` | `006360` | counterexample / 4C_success | EPC/construction quality break as hard 4C block | Reused from R10 only as C05 hard-4C counterexample: a legal/quality break must dominate contract/backlog narratives. | true | same symbol/entry appears in R10 C30, but this loop uses it as C05 EPC-quality hard-4C override; partial independent weight. |


## 8. Positive vs Counterexample Balance

| count field | value |
|---|---:|
| positive_case_count | 2 |
| counterexample_count | 3 |
| 4B_case_count | 4 |
| 4C/watch case_count | 2 |
| calibration_usable_case_count | 5 |
| calibration_usable_trigger_count | 5 |
| new_independent_case_count | 5 |
| reused_case_count | 3 |

The positive cases do not re-prove the global Stage2 bonus. They test whether C05 needs a **backlog-to-margin bridge** before Green. Counterexamples test whether contract/backlog or valuation headlines should remain Stage2/watch when margin conversion is missing or legal quality breaks appear.

## 9. Evidence Source Map

| case | evidence source class | what is allowed for scoring | what is blocked |
|---|---|---|---|
| 삼성E&A | EPC earnings/orderbook reset | Stage2/Yellow if margin bridge is visible | Green if revision confirmation is still weak |
| 현대건설 | overseas EPC backlog quality | Stage2-Actionable for order/customer quality | Green while domestic drag and margin uncertainty remain |
| 대우건설 | orderbook headline | Stage2 watch only | positive promotion without margin/revision conversion |
| DL이앤씨 | valuation/orderbook rebound | short-lived watch | Green/Yellow if margin conversion evidence is absent |
| GS건설 | quality/legal break | hard 4C override | any positive contract/backlog interpretation after thesis break |

## 10. Price Data Source Map

| symbol | company | profile_path | shard_path | corporate_action_window_status |
|---:|---|---|---|---|
| 028050 | 삼성E&A | atlas/symbol_profiles/028/028050.json | atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv | clean_180D_window |
| 000720 | 현대건설 | atlas/symbol_profiles/000/000720.json | atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv | clean_180D_window |
| 047040 | 대우건설 | atlas/symbol_profiles/047/047040.json | atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv | clean_180D_window |
| 375500 | DL이앤씨 | atlas/symbol_profiles/375/375500.json | atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv | clean_180D_window |
| 006360 | GS건설 | atlas/symbol_profiles/006/006360.json | atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv | clean_180D_window |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | type | entry | price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | verdict | usable |
|---|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|
| `R1L11_C05_028050_STAGE2A_20240131` | `028050` | Stage2-Actionable | 2024-01-31 | 22300 | 26.23 | 26.23 | 26.23 | -0.22 | -0.22 | -8.74 | current_profile_correct | true |
| `R1L11_C05_000720_STAGE2A_20240125` | `000720` | Stage2-Actionable | 2024-01-25 | 32050 | 10.76 | 12.32 | 12.32 | -2.65 | -2.65 | -13.26 | current_profile_too_early | true |
| `R1L11_C05_047040_STAGE2WATCH_20240131` | `047040` | Stage2 | 2024-01-31 | 3935 | 4.7 | 4.7 | 12.07 | -7.88 | -11.44 | -12.45 | current_profile_false_positive | true |
| `R1L11_C05_375500_FALSEGREEN_20240110` | `375500` | Stage2-Actionable | 2024-01-10 | 40750 | 8.34 | 8.34 | 8.34 | -7.73 | -21.6 | -27.85 | current_profile_false_positive | true |
| `R1L11_C05_006360_4C_20230706` | `006360` | Stage4C | 2023-07-06 | 14520 | 3.86 | 5.03 | 19.83 | -6.96 | -12.74 | -12.74 | current_profile_4C_too_late | true |


## 12. Trigger-Level OHLC Backtest Tables

Same as Section 11, with 30D/90D/180D MFE/MAE calculated from `entry_price = c` on the entry date. The representative trigger for each case is deduped for aggregate.

## 13. Current Calibrated Profile Stress Test

| question | C05 answer |
|---|---|
| How would P0 judge the cases? | It correctly keeps the clean Samsung E&A row as high-quality watch, but it can still be too early on overseas-backlog and valuation/orderbook headlines. |
| Does judgment align with MFE/MAE? | Mixed: Samsung E&A has clean upside/low initial MAE, while 대우건설/DL이앤씨 produce poor 90D/180D alignment. |
| Is Stage2 bonus too high? | Not globally; too high for C05 if margin bridge is absent. |
| Is Yellow threshold 75 too high/low? | Appropriate only when margin/revision bridge is present; otherwise too permissive. |
| Is Green threshold/revision gate adequate? | Needs C05-specific margin_bridge >= 60 and revision >= 50/55 guard. |
| Is price-only blowoff guard adequate? | Kept and strengthened for EPC orderbook rallies. |
| Is full 4B non-price requirement adequate? | Kept; price-only local peaks are risk watches, not full 4B. |
| Is hard 4C routing adequate? | Kept and strengthened for quality/legal EPC breaks. |

## 14. Stage2 / Yellow / Green Comparison

C05 should keep Stage2 early, but only after `contract_score + backlog_visibility_score + customer_quality_score` are supported. Yellow/Green requires `margin_bridge_score` and `revision_score`; otherwise the engine is reading a contract headline as if it were already P&L conversion.

`green_lateness_ratio` is directly computable only for the 삼성E&A row: `0.46`, meaning Green would be somewhat late but not useless if delayed until margin/revision confirmation. For the other rows there is no clean confirmed Green trigger.

## 15. 4B Local vs Full-window Timing Audit

| symbol | local proximity | full-window proximity | verdict |
|---:|---:|---:|---|
| 028050 | 0.88 | 0.88 | local peak requires valuation/revision slowdown before full 4B |
| 000720 | 0.88 | 0.88 | local peak, but price-only 4B is insufficient |
| 047040 | 0.72 | 0.38 | price-only local 4B too early if no margin evidence |
| 375500 | 0.98 | 0.98 | local risk watch worked, but non-price evidence needed for full 4B |
| 006360 | n/a | n/a | hard 4C, not 4B timing row |

## 16. 4C Protection Audit

GS건설 is the hard 4C anchor. C05-specific 4C should fire when quality/legal trust break evidence dominates the contract/backlog narrative. 대우건설 and DL이앤씨 remain thesis-break watch rows, not hard 4C rows.

## 17. Sector-Specific Rule Candidate

`rule_scope = sector_specific`

For `L1_INDUSTRIALS_INFRA_DEFENSE_GRID`, EPC rows need a conversion bridge:

```text
if canonical_archetype_id == C05_EPC_MEGA_CONTRACT_MARGIN_GAP:
    positive Stage2 is allowed on contract/backlog/customer quality
    Stage3-Green requires margin_bridge_score >= 60 and revision_score >= 50/55
    if execution_risk_score >= 65 or legal_or_contract_risk_score >= 65:
        cap at Stage2/watch or route to 4C if thesis break evidence is explicit
```

## 18. Canonical-Archetype Rule Candidate

`rule_scope = canonical_archetype_specific`

C05 needs a separate guard from C01/C02/C03:

1. `contract_score` alone should not lift Green.
2. `backlog_visibility_score` is positive only if delivery and margin timing are clear.
3. `margin_bridge_score` is the decisive Green gate.
4. `legal_or_contract_risk_score` and `execution_risk_score` must override contract/backlog positives.

## 19. Before / After Backtest Comparison

| profile_id | scope | eligible | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | FPR | verdict |
|---|---|---:|---:|---:|---:|---:|---:|---|
| `P0_e2r_2_1_stock_web_calibrated_proxy` | current_proxy | 5 | 11.32 | -9.73 | 15.76 | -15.01 | 0.4 | mixed; orderbook/valuation can still overpromote EPC rows |
| `P0b_e2r_2_0_baseline_reference` | rollback_reference | 5 | 11.32 | -9.73 | 15.76 | -15.01 | 0.6 | worse; headline/backlog too easily becomes Stage3 |
| `P1_L1_sector_EPC_margin_candidate` | sector_specific | 5 | 11.32 | -9.73 | 15.76 | -15.01 | 0.2 | improved; positive case remains Stage2/Yellow until bridge confirms |
| `P2_C05_archetype_EPC_bridge_candidate` | canonical_archetype_specific | 5 | 11.32 | -9.73 | 15.76 | -15.01 | 0.0 | best; explains positive and false-positive split |
| `P3_C05_counterexample_guard` | counterexample_guard | 3 | 5.83 | -15.26 | 13.33 | -17.68 | 0.0 | guardrail improves counterexample classification |


## 20. Score-Return Alignment Matrix

| trigger | before score/stage | after score/stage | changed logic | 90D MFE/MAE | alignment |
|---|---|---|---|---|---|
| `R1L11_C05_028050_STAGE2A_20240131` | 78 / Stage3-Yellow | 86 / Stage3-Yellow_high_quality_watch_not_Green_until_revision>=55 | C05 rewards margin bridge, but keeps Green gated until revision and multi-quarter conversion are confirmed. | 26.23 / -0.22 | improved_C05_alignment |
| `R1L11_C05_000720_STAGE2A_20240125` | 79 / Stage3-Yellow_or_Actionable | 73 / Stage2-Actionable_only | C05 downgrades EPC orderbook when margin bridge is not yet visible and domestic balance-sheet drag remains active. | 12.32 / -2.65 | improved_C05_alignment |
| `R1L11_C05_047040_STAGE2WATCH_20240131` | 72 / Stage2-Actionable_by_headline | 61 / Stage1_or_Stage2_Watch | C05 blocks positive promotion when contract/backlog is not accompanied by margin/revision conversion. | 4.7 / -11.44 | improved_C05_alignment |
| `R1L11_C05_375500_FALSEGREEN_20240110` | 76 / Stage2-Actionable_or_Yellow | 57 / Rejected_or_Risk_Watch | C05 valuation/orderbook bounce must not become Green without realized EPC margin bridge. | 8.34 / -21.6 | improved_C05_alignment |
| `R1L11_C05_006360_4C_20230706` | 44 / Stage4C_watch | 35 / Stage4C_Hard_Thesis_Break | C05 hard-4C override: legal/quality break cancels positive contract/backlog interpretation. | 5.03 / -12.74 | improved_C05_alignment |


## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | EPC_MEGA_CONTRACT_BACKLOG_MARGIN_CONVERSION_GUARD | 2 | 3 | 4 | 1 | 5 | 3 | 5 | 5 | 4 | true | true | C05 now has positive/counterexample/4C coverage, but needs more non-construction EPC exporters in future loops |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 5
reused_case_count: 3
reused_case_ids:
  - R1L11_C05_HYUNDAIENG_OVERSEAS_EPC_20240125
  - R1L11_C05_DLEC_VALUATION_CONTRACT_GAP_20240110
  - R1L11_C05_GSENG_QUALITY_4C_20230706
new_symbol_count: 2
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - current_profile_too_early
  - current_profile_false_positive
  - current_profile_4C_too_late
new_axis_proposed: null
existing_axis_strengthened:
  - C05-specific backlog-to-margin Green bridge
  - C05 execution/legal drag
  - C05 hard 4C quality/legal override
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated: stock-web entry rows, 30D/90D/180D path metrics, C05 evidence separation, P0 stress test, local/full-window 4B split, hard 4C override logic.

Not validated: live recommendation, production code behavior, current 2026 candidate scan, corporate-action-adjusted returns, broker execution, or exact analyst consensus revisions.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C05_margin_bridge_required_before_green,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,0,1,+1,"EPC order/backlog headline needs margin/revision conversion before Green","false positive rate fell from 40% to 0% in proxy comparison","R1L11_C05_028050_STAGE2A_20240131|R1L11_C05_000720_STAGE2A_20240125|R1L11_C05_047040_STAGE2WATCH_20240131|R1L11_C05_375500_FALSEGREEN_20240110|R1L11_C05_006360_4C_20230706",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C05_legal_quality_hard_4C_override,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,0,1,+1,"quality/legal break cancels positive contract interpretation","keeps GS건설-style hard 4C from being treated as value recovery","R1L11_C05_006360_4C_20230706",1,1,1,medium,canonical_shadow_only,"not production; 4C overlay only"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R1L11_C05_SAMSUNGEA_MARGIN_BRIDGE_20240131", "symbol": "028050", "company_name": "삼성E&A", "round": "R1", "loop": "11", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "EPC_MEGA_CONTRACT_BACKLOG_MARGIN_CONVERSION_GUARD", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R1L11_C05_028050_STAGE2A_20240131", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "aligned_positive_or_guardrail", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "EPC headline alone had been noisy, but low entry after earnings reset created a clean test of backlog-to-margin bridge instead of pure orderbook excitement."}
{"row_type": "case", "case_id": "R1L11_C05_HYUNDAIENG_OVERSEAS_EPC_20240125", "symbol": "000720", "company_name": "현대건설", "round": "R1", "loop": "11", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "EPC_MEGA_CONTRACT_BACKLOG_MARGIN_CONVERSION_GUARD", "case_type": "stage2_promote_candidate", "positive_or_counterexample": "positive", "best_trigger": "R1L11_C05_000720_STAGE2A_20240125", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "same symbol was used in R10 C30, but C05 uses a new overseas EPC backlog/margin trigger family; count with partial independent weight.", "independent_evidence_weight": 0.5, "score_price_alignment": "residual_error_or_counterexample", "current_profile_verdict": "current_profile_too_early", "price_source": "Songdaiki/stock-web", "notes": "Same symbol appeared in R10 for PF guard, but this row reuses it only for a different C05 trigger family: overseas EPC backlog quality versus margin conversion."}
{"row_type": "case", "case_id": "R1L11_C05_DAEWOOENG_ORDERBOOK_MARGIN_GAP_20240131", "symbol": "047040", "company_name": "대우건설", "round": "R1", "loop": "11", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "EPC_MEGA_CONTRACT_BACKLOG_MARGIN_CONVERSION_GUARD", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R1L11_C05_047040_STAGE2WATCH_20240131", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "residual_error_or_counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Adds a new C05 symbol where orderbook/backlog optics did not convert into clean 90D/180D price reward."}
{"row_type": "case", "case_id": "R1L11_C05_DLEC_VALUATION_CONTRACT_GAP_20240110", "symbol": "375500", "company_name": "DL이앤씨", "round": "R1", "loop": "11", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "EPC_MEGA_CONTRACT_BACKLOG_MARGIN_CONVERSION_GUARD", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R1L11_C05_375500_FALSEGREEN_20240110", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "same symbol/entry appears in R10 C30, but this loop reuses it for a C05 EPC margin-gap failure mode with partial independent weight.", "independent_evidence_weight": 0.5, "score_price_alignment": "residual_error_or_counterexample", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Reused from R10 only as new C05 margin-gap counterexample; the same price row now tests EPC/contract conversion, not PF-balance-sheet survival."}
{"row_type": "case", "case_id": "R1L11_C05_GSENG_QUALITY_4C_20230706", "symbol": "006360", "company_name": "GS건설", "round": "R1", "loop": "11", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "EPC_MEGA_CONTRACT_BACKLOG_MARGIN_CONVERSION_GUARD", "case_type": "4C_success", "positive_or_counterexample": "counterexample", "best_trigger": "R1L11_C05_006360_4C_20230706", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "same symbol/entry appears in R10 C30, but this loop uses it as C05 EPC-quality hard-4C override; partial independent weight.", "independent_evidence_weight": 0.5, "score_price_alignment": "residual_error_or_counterexample", "current_profile_verdict": "current_profile_4C_too_late", "price_source": "Songdaiki/stock-web", "notes": "Reused from R10 only as C05 hard-4C counterexample: a legal/quality break must dominate contract/backlog narratives."}
{"row_type": "trigger", "trigger_id": "R1L11_C05_028050_STAGE2A_20240131", "case_id": "R1L11_C05_SAMSUNGEA_MARGIN_BRIDGE_20240131", "symbol": "028050", "company_name": "삼성E&A", "round": "R1", "loop": "11", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "EPC_MEGA_CONTRACT_BACKLOG_MARGIN_CONVERSION_GUARD", "sector": "industrials_infra_defense_grid", "primary_archetype": "EPC mega contract / backlog margin conversion gap", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|green_strictness_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-31", "evidence_available_at_that_date": "post-result/orderbook reset; non-price margin-bridge proxy from public historical disclosures; stock-web row used for entry and path", "evidence_source": "post-result/orderbook reset; non-price margin-bridge proxy from public historical disclosures; stock-web row used for entry and path", "stage2_evidence_fields": ["public_event_or_disclosure", "backlog_or_delivery_visibility", "customer_or_order_quality"], "stage3_evidence_fields": ["margin_bridge", "financial_visibility", "multiple_public_sources", "low_red_team_risk"], "stage4b_evidence_fields": ["price_only_local_peak", "valuation_blowoff"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/028/028050/2024.csv", "profile_path": "atlas/symbol_profiles/028/028050.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-31", "entry_price": 22300, "MFE_30D_pct": 26.23, "MFE_90D_pct": 26.23, "MFE_180D_pct": 26.23, "MFE_1Y_pct": 34.98, "MFE_2Y_pct": null, "MAE_30D_pct": -0.22, "MAE_90D_pct": -0.22, "MAE_180D_pct": -8.74, "MAE_1Y_pct": -11.88, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-15", "peak_price": 28150, "drawdown_after_peak_pct": -26.29, "green_lateness_ratio": 0.46, "four_b_local_peak_proximity": 0.88, "four_b_full_window_peak_proximity": 0.88, "four_b_timing_verdict": "local_price_peak_needs_valuation_or_revision_slowdown_before_full_4B", "four_b_evidence_type": ["price_only", "valuation_blowoff"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "margin_bridge_positive_but_not_price_only_green", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "028050:2024-01-31:22300", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R1L11_C05_000720_STAGE2A_20240125", "case_id": "R1L11_C05_HYUNDAIENG_OVERSEAS_EPC_20240125", "symbol": "000720", "company_name": "현대건설", "round": "R1", "loop": "11", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "EPC_MEGA_CONTRACT_BACKLOG_MARGIN_CONVERSION_GUARD", "sector": "industrials_infra_defense_grid", "primary_archetype": "EPC mega contract / backlog margin conversion gap", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|green_strictness_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-25", "evidence_available_at_that_date": "overseas/orderbook quality historical proxy; stock-web price row used for entry and path", "evidence_source": "overseas/orderbook quality historical proxy; stock-web price row used for entry and path", "stage2_evidence_fields": ["customer_or_order_quality", "backlog_or_delivery_visibility", "relative_strength"], "stage3_evidence_fields": ["multiple_public_sources", "financial_visibility"], "stage4b_evidence_fields": ["price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000720/2024.csv", "profile_path": "atlas/symbol_profiles/000/000720.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-25", "entry_price": 32050, "MFE_30D_pct": 10.76, "MFE_90D_pct": 12.32, "MFE_180D_pct": 12.32, "MFE_1Y_pct": 12.32, "MFE_2Y_pct": null, "MAE_30D_pct": -2.65, "MAE_90D_pct": -2.65, "MAE_180D_pct": -13.26, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-05-09", "peak_price": 36000, "drawdown_after_peak_pct": -33.06, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.88, "four_b_full_window_peak_proximity": 0.88, "four_b_timing_verdict": "local_peak_but_full_4B_requires_non_price_evidence", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "limited_stage2_success_then_margin_sector_drawdown", "current_profile_verdict": "current_profile_too_early", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "000720:2024-01-25:32050", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same symbol was used in R10 C30, but C05 uses a new overseas EPC backlog/margin trigger family; count with partial independent weight.", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R1L11_C05_047040_STAGE2WATCH_20240131", "case_id": "R1L11_C05_DAEWOOENG_ORDERBOOK_MARGIN_GAP_20240131", "symbol": "047040", "company_name": "대우건설", "round": "R1", "loop": "11", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "EPC_MEGA_CONTRACT_BACKLOG_MARGIN_CONVERSION_GUARD", "sector": "industrials_infra_defense_grid", "primary_archetype": "EPC mega contract / backlog margin conversion gap", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|green_strictness_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2", "trigger_date": "2024-01-31", "evidence_available_at_that_date": "orderbook/overseas project headline proxy; stock-web price row used for entry and path", "evidence_source": "orderbook/overseas project headline proxy; stock-web price row used for entry and path", "stage2_evidence_fields": ["public_event_or_disclosure", "backlog_or_delivery_visibility"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["margin_or_backlog_slowdown", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/047/047040/2024.csv", "profile_path": "atlas/symbol_profiles/047/047040.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-31", "entry_price": 3935, "MFE_30D_pct": 4.7, "MFE_90D_pct": 4.7, "MFE_180D_pct": 12.07, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -7.88, "MAE_90D_pct": -11.44, "MAE_180D_pct": -12.45, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-19", "peak_price": 4120, "drawdown_after_peak_pct": -18.2, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.72, "four_b_full_window_peak_proximity": 0.38, "four_b_timing_verdict": "price_only_local_4B_too_early_if_no_margin_slowdown_evidence", "four_b_evidence_type": ["price_only", "margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "orderbook_headline_failed_to_rerate", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "047040:2024-01-31:3935", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R1L11_C05_375500_FALSEGREEN_20240110", "case_id": "R1L11_C05_DLEC_VALUATION_CONTRACT_GAP_20240110", "symbol": "375500", "company_name": "DL이앤씨", "round": "R1", "loop": "11", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "EPC_MEGA_CONTRACT_BACKLOG_MARGIN_CONVERSION_GUARD", "sector": "industrials_infra_defense_grid", "primary_archetype": "EPC mega contract / backlog margin conversion gap", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|green_strictness_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-10", "evidence_available_at_that_date": "valuation/orderbook rebound proxy; stock-web price row used for entry and path", "evidence_source": "valuation/orderbook rebound proxy; stock-web price row used for entry and path", "stage2_evidence_fields": ["valuation_repricing_score", "relative_strength"], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["price_only_local_peak", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv", "profile_path": "atlas/symbol_profiles/375/375500.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-10", "entry_price": 40750, "MFE_30D_pct": 8.34, "MFE_90D_pct": 8.34, "MFE_180D_pct": 8.34, "MFE_1Y_pct": 8.34, "MFE_2Y_pct": null, "MAE_30D_pct": -7.73, "MAE_90D_pct": -21.6, "MAE_180D_pct": -27.85, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-02", "peak_price": 44150, "drawdown_after_peak_pct": -33.41, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.98, "four_b_timing_verdict": "good_local_risk_watch_but_not_full_4B_without_margin_slowdown_evidence", "four_b_evidence_type": ["price_only", "margin_or_backlog_slowdown"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "valuation_repricing_failed_to_hold", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "375500:2024-01-10:40750", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same symbol/entry appears in R10 C30, but this loop reuses it for a C05 EPC margin-gap failure mode with partial independent weight.", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "R1L11_C05_006360_4C_20230706", "case_id": "R1L11_C05_GSENG_QUALITY_4C_20230706", "symbol": "006360", "company_name": "GS건설", "round": "R1", "loop": "11", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "EPC_MEGA_CONTRACT_BACKLOG_MARGIN_CONVERSION_GUARD", "sector": "industrials_infra_defense_grid", "primary_archetype": "EPC mega contract / backlog margin conversion gap", "loop_objective": "coverage_gap_fill|counterexample_mining|sector_specific_rule_discovery|green_strictness_stress_test|4C_thesis_break_timing_test", "trigger_type": "Stage4C", "trigger_date": "2023-07-06", "evidence_available_at_that_date": "quality/legal incident proxy; stock-web price row used for entry and path", "evidence_source": "quality/legal incident proxy; stock-web price row used for entry and path", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["legal_or_regulatory_block", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["accounting_or_trust_break", "thesis_evidence_broken", "legal_or_regulatory_block"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/006/006360/2023.csv", "profile_path": "atlas/symbol_profiles/006/006360.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2023-07-06", "entry_price": 14520, "MFE_30D_pct": 3.86, "MFE_90D_pct": 5.03, "MFE_180D_pct": 19.83, "MFE_1Y_pct": 19.83, "MFE_2Y_pct": null, "MAE_30D_pct": -6.96, "MAE_90D_pct": -12.74, "MAE_180D_pct": -12.74, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2023-11-23", "peak_price": 17400, "drawdown_after_peak_pct": -13.22, "green_lateness_ratio": "not_applicable:4C_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_4C", "four_b_evidence_type": ["legal_or_regulatory_block", "margin_or_backlog_slowdown"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "quality_legal_thesis_break_blocks_false_green", "current_profile_verdict": "current_profile_4C_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "006360:2023-07-06:14520", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": "same symbol/entry appears in R10 C30, but this loop uses it as C05 EPC-quality hard-4C override; partial independent weight.", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C05_shadow", "case_id": "R1L11_C05_SAMSUNGEA_MARGIN_BRIDGE_20240131", "trigger_id": "R1L11_C05_028050_STAGE2A_20240131", "symbol": "028050", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "raw_component_scores_before": {"contract_score": 70, "backlog_visibility_score": 68, "margin_bridge_score": 60, "revision_score": 45, "relative_strength_score": 42, "customer_quality_score": 65, "policy_or_regulatory_score": 20, "valuation_repricing_score": 48, "execution_risk_score": 35, "legal_or_contract_risk_score": 20, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 78, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 72, "backlog_visibility_score": 72, "margin_bridge_score": 72, "revision_score": 52, "relative_strength_score": 44, "customer_quality_score": 68, "policy_or_regulatory_score": 20, "valuation_repricing_score": 50, "execution_risk_score": 30, "legal_or_contract_risk_score": 18, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 86, "stage_label_after": "Stage3-Yellow_high_quality_watch_not_Green_until_revision>=55", "changed_components": ["margin_bridge_score", "revision_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "C05 rewards margin bridge, but keeps Green gated until revision and multi-quarter conversion are confirmed.", "MFE_90D_pct": 26.23, "MAE_90D_pct": -0.22, "score_return_alignment_label": "improved_C05_alignment", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C05_shadow", "case_id": "R1L11_C05_HYUNDAIENG_OVERSEAS_EPC_20240125", "trigger_id": "R1L11_C05_000720_STAGE2A_20240125", "symbol": "000720", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "raw_component_scores_before": {"contract_score": 72, "backlog_visibility_score": 70, "margin_bridge_score": 42, "revision_score": 38, "relative_strength_score": 52, "customer_quality_score": 68, "policy_or_regulatory_score": 30, "valuation_repricing_score": 45, "execution_risk_score": 48, "legal_or_contract_risk_score": 38, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 79, "stage_label_before": "Stage3-Yellow_or_Actionable", "raw_component_scores_after": {"contract_score": 72, "backlog_visibility_score": 70, "margin_bridge_score": 35, "revision_score": 34, "relative_strength_score": 52, "customer_quality_score": 68, "policy_or_regulatory_score": 30, "valuation_repricing_score": 42, "execution_risk_score": 55, "legal_or_contract_risk_score": 42, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 73, "stage_label_after": "Stage2-Actionable_only", "changed_components": ["margin_bridge_score", "revision_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "C05 downgrades EPC orderbook when margin bridge is not yet visible and domestic balance-sheet drag remains active.", "MFE_90D_pct": 12.32, "MAE_90D_pct": -2.65, "score_return_alignment_label": "improved_C05_alignment", "current_profile_verdict": "current_profile_too_early"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C05_shadow", "case_id": "R1L11_C05_DAEWOOENG_ORDERBOOK_MARGIN_GAP_20240131", "trigger_id": "R1L11_C05_047040_STAGE2WATCH_20240131", "symbol": "047040", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "raw_component_scores_before": {"contract_score": 66, "backlog_visibility_score": 62, "margin_bridge_score": 28, "revision_score": 28, "relative_strength_score": 35, "customer_quality_score": 50, "policy_or_regulatory_score": 25, "valuation_repricing_score": 38, "execution_risk_score": 58, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 72, "stage_label_before": "Stage2-Actionable_by_headline", "raw_component_scores_after": {"contract_score": 60, "backlog_visibility_score": 54, "margin_bridge_score": 22, "revision_score": 24, "relative_strength_score": 28, "customer_quality_score": 45, "policy_or_regulatory_score": 20, "valuation_repricing_score": 30, "execution_risk_score": 65, "legal_or_contract_risk_score": 48, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 61, "stage_label_after": "Stage1_or_Stage2_Watch", "changed_components": ["margin_bridge_score", "revision_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "C05 blocks positive promotion when contract/backlog is not accompanied by margin/revision conversion.", "MFE_90D_pct": 4.7, "MAE_90D_pct": -11.44, "score_return_alignment_label": "improved_C05_alignment", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C05_shadow", "case_id": "R1L11_C05_DLEC_VALUATION_CONTRACT_GAP_20240110", "trigger_id": "R1L11_C05_375500_FALSEGREEN_20240110", "symbol": "375500", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "raw_component_scores_before": {"contract_score": 55, "backlog_visibility_score": 52, "margin_bridge_score": 24, "revision_score": 25, "relative_strength_score": 58, "customer_quality_score": 40, "policy_or_regulatory_score": 20, "valuation_repricing_score": 60, "execution_risk_score": 58, "legal_or_contract_risk_score": 40, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable_or_Yellow", "raw_component_scores_after": {"contract_score": 48, "backlog_visibility_score": 46, "margin_bridge_score": 18, "revision_score": 22, "relative_strength_score": 46, "customer_quality_score": 35, "policy_or_regulatory_score": 15, "valuation_repricing_score": 45, "execution_risk_score": 68, "legal_or_contract_risk_score": 45, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 57, "stage_label_after": "Rejected_or_Risk_Watch", "changed_components": ["margin_bridge_score", "revision_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "C05 valuation/orderbook bounce must not become Green without realized EPC margin bridge.", "MFE_90D_pct": 8.34, "MAE_90D_pct": -21.6, "score_return_alignment_label": "improved_C05_alignment", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C05_shadow", "case_id": "R1L11_C05_GSENG_QUALITY_4C_20230706", "trigger_id": "R1L11_C05_006360_4C_20230706", "symbol": "006360", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "raw_component_scores_before": {"contract_score": 40, "backlog_visibility_score": 42, "margin_bridge_score": 10, "revision_score": 15, "relative_strength_score": 20, "customer_quality_score": 15, "policy_or_regulatory_score": 5, "valuation_repricing_score": 20, "execution_risk_score": 82, "legal_or_contract_risk_score": 88, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 78}, "weighted_score_before": 44, "stage_label_before": "Stage4C_watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 0, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 0, "execution_risk_score": 92, "legal_or_contract_risk_score": 95, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 88}, "weighted_score_after": 35, "stage_label_after": "Stage4C_Hard_Thesis_Break", "changed_components": ["margin_bridge_score", "revision_score", "execution_risk_score", "legal_or_contract_risk_score"], "component_delta_explanation": "C05 hard-4C override: legal/quality break cancels positive contract/backlog interpretation.", "MFE_90D_pct": 5.03, "MAE_90D_pct": -12.74, "score_return_alignment_label": "improved_C05_alignment", "current_profile_verdict": "current_profile_4C_too_late"}
{"row_type": "residual_contribution", "round": "R1", "loop": "11", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "new_independent_case_count": 5, "reused_case_count": 3, "new_symbol_count": 2, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_total_min", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["current_profile_too_early", "current_profile_false_positive", "current_profile_4C_too_late"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
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
completed_loop = 11
next_round = R2
next_loop = 11
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- `reports/e2r_calibration/by_round/R1.md` was used for coverage context only.
- `Songdaiki/stock-web` manifest/schema/profile/shards were used as the historical OHLC atlas.
- No `stock_agent/src/e2r` code was read or patched in this research step.

