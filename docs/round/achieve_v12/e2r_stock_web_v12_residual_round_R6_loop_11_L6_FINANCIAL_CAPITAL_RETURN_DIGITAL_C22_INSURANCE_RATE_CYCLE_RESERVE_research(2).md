# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

- research_session: `post_calibrated_sector_archetype_residual_research`
- mode: `historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12`
- output_file: `e2r_stock_web_v12_residual_round_R6_loop_11_L6_FINANCIAL_CAPITAL_RETURN_DIGITAL_C22_INSURANCE_RATE_CYCLE_RESERVE_research.md`
- scheduled_round: `R6`
- scheduled_loop: `11`
- completed_round: `R6`
- completed_loop: `11`
- next_round: `R7`
- next_loop: `11`
- round_schedule_status: `valid`
- round_sector_consistency: `pass`
- large_sector_id: `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL`
- canonical_archetype_id: `C22_INSURANCE_RATE_CYCLE_RESERVE`
- fine_archetype_id: `INSURANCE_IFRS17_CSM_RESERVE_QUALITY_CAPITAL_RETURN`
- loop_objective: `coverage_gap_fill | counterexample_mining | 4B_non_price_requirement_stress_test | 4C_thesis_break_timing_test | sector_specific_rule_discovery | canonical_archetype_compression`
- production_scoring_changed: `false`
- shadow_weight_only: `true`
- handoff_prompt_embedded: `true`
- handoff_prompt_executed_now: `false`

This loop adds **5** new independent cases, **3** counterexamples, and **3** residual errors for `R6/L6/C22`.

## 1. Current Calibrated Profile Assumption

Assumed current profile is `e2r_2_1_stock_web_calibrated_proxy`. Existing global axes are not re-proposed. This loop stress-tests them inside insurance/IFRS17 and proposes only shadow-only sector/canonical refinements.

Current global assumptions kept: `stage2_actionable_evidence_bonus=+2.0`, `stage3_yellow_total_min=75`, `stage3_green_total_min=87`, `stage3_green_revision_min=55`, `price_only_blowoff_blocks_positive_stage=true`, `full_4b_requires_non_price_evidence=true`, `hard_4c_thesis_break_routes_to_4c=true`.

## 2. Round / Large Sector / Canonical Archetype Scope

R6 is mapped to `L6_FINANCIAL_CAPITAL_RETURN_DIGITAL` and passes the hard sector consistency gate. The selected canonical archetype is `C22_INSURANCE_RATE_CYCLE_RESERVE`, focused on non-life insurance under IFRS17: CSM growth, reserve quality, loss/claim ratio pressure, solvency/capital-return visibility, and event-premium false positives.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed stock_agent research artifacts were checked only for coverage context, not code. R6 already has 101 representative triggers and 25 unique cases, with Stage2/Stage3/4B/4C coverage present. No `C22_INSURANCE_RATE_CYCLE_RESERVE` file-level hit was found by repository search, so this loop fills a canonical compression gap rather than repeating a known C22 result.

Duplicate avoidance outcome: all five symbols are treated as new independent C22 sample rows inside this v12 loop. Same canonical archetype reuse is allowed; same symbol+same trigger reuse was not used.

## 4. Stock-Web OHLC Input / Price Source Validation

Stock-Web manifest validation:


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


The manifest reports `source_name=FinanceData/marcap`, `price_adjustment_status=raw_unadjusted_marcap`, `min_date=1995-05-02`, `max_date=2026-02-20`, `tradable_row_count=14354401`, `symbol_count=5414`, `active_like_symbol_count=2868`, and calibration shards under `atlas/ohlcv_tradable_by_symbol_year`. Therefore every forward window is judged against `2026-02-20`, not the current calendar date.

## 5. Historical Eligibility Gate

All representative entry rows use stock-web tradable shards, have at least 180 trading days forward, and have no 2023-2024 corporate-action candidate overlap in the entry~D+180 windows. Old corporate-action candidates exist for some long-lived insurers, but they are outside the tested windows.


| symbol | company | profile caveat | tested window status | calibration_usable |
|---|---:|---|---|---|

| 000810 | 삼성화재 | old CA candidates 1999-2000 only; clean 2023-2024 window | clean_180D_window | true |

| 005830 | DB손해보험 | old CA candidate 1999 only; clean 2023-2024 window | clean_180D_window | true |

| 001450 | 현대해상 | old CA candidate 2004 only; clean 2023-2024 window | clean_180D_window | true |

| 000370 | 한화손해보험 | old CA candidates through 2017 only; clean 2023-2024 window | clean_180D_window | true |

| 000400 | 롯데손해보험 | old CA candidates through 2019 only; clean 2024 window | clean_180D_window | true |



## 6. Canonical Archetype Compression Map

C22 should compress noisy insurance micro-narratives into four signal buckets:

1. **CSM/IFRS17 quality**: CSM growth and new accounting visibility are necessary but not sufficient.
2. **Reserve/claim-ratio quality**: poor reserve or loss-ratio pressure blocks generic IFRS17 promotion.
3. **Capital-return visibility**: ROE/PBR rerating is stronger when dividend/buyback/solvency path is visible.
4. **Event-premium guard**: M&A or value-up price spikes are 4B/4C overlays, not clean Stage2/Stage3 promotion.

## 7. Case Selection Summary

| case_id | symbol | company | role | verdict | why selected |
|---|---:|---|---|---|---|

| R6L11-C22-000810-20230515 | 000810 | 삼성화재 | positive_structural_success | current_profile_correct | IFRS17 전환 후 보장성/CSM·자본환원 기대가 같이 붙은 대형 손보 positive 표본. |

| R6L11-C22-005830-20230515 | 005830 | DB손해보험 | positive_delayed_structural | current_profile_too_late | 초기 90D는 흔들렸지만 180D부터 CSM/ROE 재평가가 가격에 반영된 지연 positive 표본. |

| R6L11-C22-001450-20230515 | 001450 | 현대해상 | reserve_quality_counterexample | current_profile_false_positive | 같은 IFRS17 보험 basket이어도 예실차/손해율/준비금 부담이 있으면 Stage2 promotion이 과해지는 반례. |

| R6L11-C22-000370-20230515 | 000370 | 한화손해보험 | high_mae_counterexample | current_profile_false_positive | 보험 beta는 있으나 자본환원/CSM 질이 확인되기 전에는 180D 보상이 작고 MAE가 커지는 반례. |

| R6L11-C22-000400-20240201 | 000400 | 롯데손해보험 | price_only_event_counterexample | current_profile_correct | 매각/이벤트 프리미엄성 거래량 폭발은 30D MFE가 커도 C22 구조적 Stage3 승격에는 쓰면 안 되는 반례. |



## 8. Positive vs Counterexample Balance

- positive_case_count: `2` — 삼성화재, DB손해보험.
- counterexample_count: `3` — 현대해상, 한화손해보험, 롯데손해보험.
- 4B_case_count: `2` — 삼성화재 price-only local 4B-too-early, 롯데손보 event-premium 4B.
- 4C_case_count: `1` — 롯데손보 event-premium thesis-break/protection.

This balance is deliberately asymmetric: C22 needs more false-positive guards than more proof that insurance can rerate.

## 9. Evidence Source Map

This MD intentionally separates price validation from event evidence. Exact DART/KIND/report IDs should be attached later during ingestion. The backtest itself uses only stock-web OHLC.

| family | evidence used now | implementation attachment needed later |
|---|---|---|
| IFRS17 / CSM visibility | public result context, not used as price data | quarterly reports, IR decks, analyst note identifiers |
| capital return / value-up | public market context and price response | DART disclosures, board/shareholder-return announcements |
| reserve / claim-ratio risk | counterexample label from path behavior and known insurance risk family | quarter-specific reserve/claim-ratio detail |
| M&A/event premium | price-only event-premium row for Lotte | news/disclosure ID to distinguish from C22 structural signal |

## 10. Price Data Source Map

| symbol | tradable shard | profile | entry rows inspected |
|---:|---|---|---|

| 000810 | `atlas/ohlcv_tradable_by_symbol_year/000/000810/2023.csv` | `atlas/symbol_profiles/000/000810.json` | `2023-05-15 close=227500` |

| 005830 | `atlas/ohlcv_tradable_by_symbol_year/005/005830/2023.csv` | `atlas/symbol_profiles/005/005830.json` | `2023-05-15 close=76200` |

| 001450 | `atlas/ohlcv_tradable_by_symbol_year/001/001450/2023.csv` | `atlas/symbol_profiles/001/001450.json` | `2023-05-15 close=34750` |

| 000370 | `atlas/ohlcv_tradable_by_symbol_year/000/000370/2023.csv` | `atlas/symbol_profiles/000/000370.json` | `2023-05-15 close=4380` |

| 000400 | `atlas/ohlcv_tradable_by_symbol_year/000/000400/2024.csv` | `atlas/symbol_profiles/000/000400.json` | `2024-02-01 close=2610` |



## 11. Case-by-Case Trigger Grid

| trigger_id | case_id | type | trigger_date | entry_date | entry_price | 30D MFE/MAE | 90D MFE/MAE | 180D MFE/MAE | current verdict | aggregate role |
|---|---|---|---|---:|---:|---:|---:|---:|---|---|

| R6L11-C22-000810-T1 | R6L11-C22-000810-20230515 | Stage2-Actionable | 2023-05-12 | 2023-05-15 | 227500 | 7.69 / -5.49 | 20.66 / -5.49 | 49.45 / -5.49 | current_profile_correct | representative |

| R6L11-C22-000810-T2 | R6L11-C22-000810-20230515 | Stage4B | 2024-03-21 | 2024-03-21 | 343000 | 0.87 / -12.83 | 9.62 / -12.83 | 26.24 / -12.83 | current_profile_4B_too_early | 4B_overlay_only |

| R6L11-C22-005830-T1 | R6L11-C22-005830-20230515 | Stage2-Actionable | 2023-05-12 | 2023-05-15 | 76200 | 9.58 / -3.41 | 8.53 / -7.48 | 38.32 / -7.48 | current_profile_too_late | representative |

| R6L11-C22-005830-T2 | R6L11-C22-005830-20230515 | Stage3-Green | 2024-02-02 | 2024-02-02 | 99200 | 10.89 / -8.17 | 16.94 / -8.17 | 49.19 / -8.17 | current_profile_too_late | label_comparison_only |

| R6L11-C22-001450-T1 | R6L11-C22-001450-20230515 | Stage2-Actionable_candidate_rejected | 2023-05-12 | 2023-05-15 | 34750 | 4.46 / -13.38 | 4.46 / -21.58 | 5.9 / -21.58 | current_profile_false_positive | representative |

| R6L11-C22-000370-T1 | R6L11-C22-000370-20230515 | Stage2-Actionable_candidate_rejected | 2023-05-12 | 2023-05-15 | 4380 | 13.47 / -10.96 | 13.47 / -18.72 | 13.47 / -18.72 | current_profile_false_positive | representative |

| R6L11-C22-000400-T1 | R6L11-C22-000400-20240201 | Stage2-Actionable_candidate_rejected | 2024-02-01 | 2024-02-01 | 2610 | 40.61 / -4.6 | 40.61 / -4.6 | 40.61 / -23.87 | current_profile_correct | representative |

| R6L11-C22-000400-T2 | R6L11-C22-000400-20240201 | Stage4C | 2024-10-08 | 2024-10-08 | 2235 | 6.71 / -11.1 | 13.42 / -11.1 | 17.45 / -11.1 | current_profile_correct | 4C_overlay_only |



## 12. Trigger-Level OHLC Backtest Tables

Representative rows only are used for aggregate metrics. 4B/4C overlays are kept for timing but deduped from aggregate return averages.


| symbol | entry_date | entry_price | peak_date | peak_price | MFE_180D | MAE_180D | below_entry_90D | outcome |
|---:|---|---:|---|---:|---:|---:|---|---|

| 000810 | 2023-05-15 | 227500 | 2024-03-22 | 346000 | 49.45 | -5.49 | true | structural_success |

| 005830 | 2023-05-15 | 76200 | 2024-03-14 | 110000 | 38.32 | -7.48 | true | missed_structural |

| 001450 | 2023-05-15 | 34750 | 2024-02-05 | 36800 | 5.9 | -21.58 | true | false_positive_green |

| 000370 | 2023-05-15 | 4380 | 2026-02-20 | 9300 | 13.47 | -18.72 | true | high_mae_success |

| 000400 | 2024-02-01 | 2610 | 2024-02-16 | 3670 | 40.61 | -23.87 | true | price_moved_without_evidence |


Aggregate representative result: avg_MFE_90D = `17.55`, avg_MAE_90D = `-11.57`, avg_MFE_180D = `29.55`, avg_MAE_180D = `-15.43`.

## 13. Current Calibrated Profile Stress Test

The current profile is directionally right on price-only blowoff and 4B non-price requirements, but still too coarse for C22. Generic IFRS17 evidence can overpromote 현대해상/한화손보 unless reserve-quality and claim-ratio risk are scored before Yellow/Green. DB손보 is the opposite residual: early evidence looked noisy at 90D but the 180D/1Y path argues for a sector-specific patience rule when reserve quality and capital-return visibility are improving.


| case | profile verdict | actual path | stress-test conclusion |
|---|---|---|---|

| R6L11-C22-000810-20230515 | current_profile_correct | 180D MFE 49.45 / MAE -5.49 | clean_CSM_ROE_capital_return_signal_aligned_with_180D_MFE |

| R6L11-C22-005830-20230515 | current_profile_too_late | 180D MFE 38.32 / MAE -7.48 | early_CSM_reserve_quality_signal_delayed_by_overstrict_revision_gate |

| R6L11-C22-001450-20230515 | current_profile_false_positive | 180D MFE 5.9 / MAE -21.58 | generic_IFRS17_score_failed_without_reserve_claim_ratio_penalty |

| R6L11-C22-000370-20230515 | current_profile_false_positive | 180D MFE 13.47 / MAE -18.72 | small_cap_IFRS17_beta_has_high_MAE_without_capital_return_visibility |

| R6L11-C22-000400-20240201 | current_profile_correct | 180D MFE 40.61 / MAE -23.87 | M&A_or_event_premium_spike_not_clean_C22_positive_signal |



## 14. Stage2 / Yellow / Green Comparison

DB손보의 Stage3-Green comparison row shows green_lateness_ratio ≈ `0.68`: it did not destroy the trade, but it consumed most of the early rerating from the Stage2-Actionable entry. 삼성화재 has an earlier clean Stage2-Actionable row and a later 4B row; this reinforces that in C22, early Stage2 is useful only when reserve/CSM/capital-return evidence is clean.

## 15. 4B Local vs Full-window Timing Audit

| trigger | local proximity | full-window proximity | verdict | interpretation |
|---|---:|---:|---|---|

| R6L11-C22-000810-T2 | 0.98 | 0.43 | price_only_local_4B_too_early | price_only,valuation_blowoff,positioning_overheat |

| R6L11-C22-000400-T1 | 0.72 | 0.72 | good_local_4B_but_not_positive_stage | price_only,control_premium_or_event_premium,valuation_blowoff |


삼성화재는 local proximity가 높아도 full-window proximity가 낮아 `price_only_local_4B_too_early`가 된다. 롯데손보는 local and full observed spike가 모두 event-premium 성격이므로 positive Stage로 쓰지 않고 4B/4C overlay로만 쓴다.

## 16. 4C Protection Audit

롯데손보의 2024-10-08 row는 event premium이 꺼진 뒤 구조적 C22 증거가 따라오지 않았다는 thesis-break protection row다. 2024-02-16 local peak 3,670 대비 2024-11-13 저가 1,987은 약 -45.9% drawdown이다. 4C가 늦게 붙으면 local MFE를 구조적 signal로 오인한다.

## 17. Sector-Specific Rule Candidate

`sector_specific_rule_candidate = true`

L6 보험에서는 IFRS17 headline이 Stage2 evidence가 될 수는 있지만, Stage3-Yellow/Green으로 밀어 올리려면 `capital_return_visibility_score`와 `reserve_quality_score`가 둘 다 일정 수준 이상이어야 한다. Claim-ratio/reserve red flag가 확인되면 Stage2-Actionable bonus를 제한한다.

## 18. Canonical-Archetype Rule Candidate

`canonical_archetype_rule_candidate = true`

Proposed C22 shadow rule:

```text
if canonical_archetype_id == C22_INSURANCE_RATE_CYCLE_RESERVE:
    require reserve_quality_score >= 60 for Stage3-Yellow
    require capital_return_visibility_score >= 60 for Stage3-Yellow
    require reserve_quality_score >= 70 and capital_return_visibility_score >= 65 for Stage3-Green
    if claim_ratio_risk_score >= 60 or reserve_quality_score < 45:
        cap stage at Stage2-watch unless confirmed_revision and capital_return visibility offset it
    if relative_strength_score is driven by M&A/event premium only:
        block Stage2/Stage3 promotion and route to 4B/4C overlay audit
```

## 19. Before / After Backtest Comparison

| profile | scope | eligible | avg MFE90 | avg MAE90 | avg MFE180 | avg MAE180 | FP rate | verdict |
|---|---|---:|---:|---:|---:|---:|---|---|

| P0_e2r_2_1_stock_web_calibrated_proxy | global_current | 5 | 17.55 | -11.57 | 29.55 | -15.43 | 2/5 or 40% if generic IFRS17 headline is promoted | mixed; C22 needs reserve-quality and capital-return visibility split |

| P0b_e2r_2_0_baseline_reference | rollback_reference | 5 | 17.55 | -11.57 | 29.55 | -15.43 | 3/5 if no price-only or reserve-quality guard | worse than P0 |

| P1_sector_specific_candidate_profile | sector_specific | 5 | 14.59 | -6.49 | 43.89 | -6.49 | 1/5 residual watch | better; positives stay eligible while event-premium false positives are blocked |

| P2_canonical_archetype_candidate_profile | canonical_archetype_specific | 5 | 14.59 | -6.49 | 43.89 | -6.49 | 0/5 in this loop | best local fit; proposed as shadow-only |

| P3_counterexample_guard_profile | canonical_archetype_specific | 3 | 19.51 | -14.97 | 19.99 | -21.39 | 0/3 blocked | best protection profile |



## 20. Score-Return Alignment Matrix

| trigger | before score/stage | after score/stage | MFE90/MAE90 | alignment |
|---|---|---|---|---|

| R6L11-C22-000810-T1 | 84.0 / Stage3-Yellow | 88.0 / Stage3-Green_candidate | 20.66 / -5.49 | structural_success |

| R6L11-C22-000810-T2 | 92.0 / Stage4B_price_only_watch | 90.0 / Stage4B_watch_not_full_exit | 9.62 / -12.83 | 4B_too_early |

| R6L11-C22-005830-T1 | 73.0 / Stage2-Actionable | 78.0 / Stage3-Yellow | 8.53 / -7.48 | missed_structural |

| R6L11-C22-005830-T2 | 88.0 / Stage3-Green | 88.0 / Stage3-Green | 16.94 / -8.17 | late_green_but_not_fatal |

| R6L11-C22-001450-T1 | 76.0 / Stage3-Yellow_false_positive_risk | 64.0 / Stage2_watch_or_reject | 4.46 / -21.58 | false_positive_green |

| R6L11-C22-000370-T1 | 74.0 / Stage2-Actionable_false_positive_risk | 59.0 / Stage2_watch_or_reject | 13.47 / -18.72 | high_mae_success |

| R6L11-C22-000400-T1 | 78.0 / Stage3-Yellow_if_price_overweighted | 52.0 / Stage2_watch_or_4B_event_overlay_only | 40.61 / -4.6 | price_moved_without_evidence |

| R6L11-C22-000400-T2 | 36.0 / Stage4C | 36.0 / Stage4C | 13.42 / -11.1 | 4C_success |



## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|

| L6_FINANCIAL_CAPITAL_RETURN_DIGITAL | C22_INSURANCE_RATE_CYCLE_RESERVE | INSURANCE_IFRS17_CSM_RESERVE_QUALITY_CAPITAL_RETURN | 2 | 3 | 2 | 1 | 5 | 0 | 8 | 5 | 3 | true | true | More banks/C21 and life-insurer cross-checks remain; C22 now has positive+counterexample+4B/4C seed coverage. |

## 22. Residual Contribution Summary

```yaml

new_independent_case_count: 5
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 5
new_canonical_archetype_count: 1
new_fine_archetype_count: 1
new_trigger_family_count: 5
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_yellow_total_min
  - stage3_green_total_min
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - generic_IFRS17_false_positive
  - reserve_claim_ratio_penalty_missing
  - capital_return_visibility_delayed
  - price_only_event_premium_local_MFE
new_axis_proposed: null
existing_axis_strengthened:
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
existing_axis_weakened:
  - stage3_green_revision_min: only as C22-specific patience adjustment, not global rollback
existing_axis_kept:
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated: stock-web manifest fields, tradable shard paths, symbol profiles, entry dates, entry prices, 30D/90D/180D MFE/MAE approximations from visible OHLC rows, local/full 4B split, and representative-trigger dedupe.

Not validated in this run: exact DART/KIND filing IDs, exact analyst-report text, production code mapping, live candidate status, and brokerage/API behavior. This MD is not an investment recommendation.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c22_reserve_quality_gate,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"Do not promote generic IFRS17 headline without reserve-quality and claim-ratio check","Hyundai/Hanwha false positives blocked while Samsung/DB remain eligible","R6L11-C22-001450-T1|R6L11-C22-000370-T1|R6L11-C22-000810-T1|R6L11-C22-005830-T1",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c22_capital_return_visibility_bonus,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"CSM/ROE plus capital-return visibility separates clean rerating from accounting-only signal","Samsung/DB 180D MFE remained positive after early evidence","R6L11-C22-000810-T1|R6L11-C22-005830-T1",2,2,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c22_price_only_event_premium_block,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,1,1,0,"Existing price-only blowoff guard is kept and specialized for insurance M&A/event premium","Lotte price spike had high local MFE but poor full-window alignment","R6L11-C22-000400-T1|R6L11-C22-000400-T2",1,1,1,medium,axis_stress_test,"strengthens existing axis; no new global delta"
```

## 25. Machine-Readable Rows

### 25.1 price_source_validation
```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

### 25.2 case rows
```jsonl

{"row_type": "case", "case_id": "R6L11-C22-000810-20230515", "symbol": "000810", "company_name": "삼성화재", "round": "R6", "loop": "11", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_IFRS17_CSM_RESERVE_QUALITY_CAPITAL_RETURN", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R6L11-C22-000810-T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "clean_CSM_ROE_capital_return_signal_aligned_with_180D_MFE", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "IFRS17 전환 후 보장성/CSM·자본환원 기대가 같이 붙은 대형 손보 positive 표본."}

{"row_type": "case", "case_id": "R6L11-C22-005830-20230515", "symbol": "005830", "company_name": "DB손해보험", "round": "R6", "loop": "11", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_IFRS17_CSM_RESERVE_QUALITY_CAPITAL_RETURN", "case_type": "missed_structural", "positive_or_counterexample": "positive", "best_trigger": "R6L11-C22-005830-T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "early_CSM_reserve_quality_signal_delayed_by_overstrict_revision_gate", "current_profile_verdict": "current_profile_too_late", "price_source": "Songdaiki/stock-web", "notes": "초기 90D는 흔들렸지만 180D부터 CSM/ROE 재평가가 가격에 반영된 지연 positive 표본."}

{"row_type": "case", "case_id": "R6L11-C22-001450-20230515", "symbol": "001450", "company_name": "현대해상", "round": "R6", "loop": "11", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_IFRS17_CSM_RESERVE_QUALITY_CAPITAL_RETURN", "case_type": "false_positive_green", "positive_or_counterexample": "counterexample", "best_trigger": "R6L11-C22-001450-T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "generic_IFRS17_score_failed_without_reserve_claim_ratio_penalty", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "같은 IFRS17 보험 basket이어도 예실차/손해율/준비금 부담이 있으면 Stage2 promotion이 과해지는 반례."}

{"row_type": "case", "case_id": "R6L11-C22-000370-20230515", "symbol": "000370", "company_name": "한화손해보험", "round": "R6", "loop": "11", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_IFRS17_CSM_RESERVE_QUALITY_CAPITAL_RETURN", "case_type": "high_mae_success", "positive_or_counterexample": "counterexample", "best_trigger": "R6L11-C22-000370-T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "small_cap_IFRS17_beta_has_high_MAE_without_capital_return_visibility", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "보험 beta는 있으나 자본환원/CSM 질이 확인되기 전에는 180D 보상이 작고 MAE가 커지는 반례."}

{"row_type": "case", "case_id": "R6L11-C22-000400-20240201", "symbol": "000400", "company_name": "롯데손해보험", "round": "R6", "loop": "11", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_IFRS17_CSM_RESERVE_QUALITY_CAPITAL_RETURN", "case_type": "price_moved_without_evidence", "positive_or_counterexample": "counterexample", "best_trigger": "R6L11-C22-000400-T1", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "M&A_or_event_premium_spike_not_clean_C22_positive_signal", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "매각/이벤트 프리미엄성 거래량 폭발은 30D MFE가 커도 C22 구조적 Stage3 승격에는 쓰면 안 되는 반례."}

```

### 25.3 trigger rows
```jsonl

{"row_type": "trigger", "trigger_id": "R6L11-C22-000810-T1", "case_id": "R6L11-C22-000810-20230515", "symbol": "000810", "company_name": "삼성화재", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-05-12", "entry_date": "2023-05-15", "entry_price": 227500, "evidence_available_at_that_date": "IFRS17 전환 후 1Q 손보 이익/CSM/자본여력 확인. 정확한 filing-id는 batch ingest에서 연결.", "evidence_source": "stock_web_price_only_plus_public_IFRS17_result_context__attach_DART_KRX_ids_later", "stage2_evidence_fields": ["public_event_or_disclosure", "early_revision_signal", "relative_strength", "policy_or_regulatory_optionality"], "stage3_evidence_fields": ["financial_visibility", "low_red_team_risk"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000810/2023.csv", "profile_path": "atlas/symbol_profiles/000/000810.json", "MFE_30D_pct": 7.69, "MFE_90D_pct": 20.66, "MFE_180D_pct": 49.45, "MFE_1Y_pct": 52.09, "MFE_2Y_pct": 171.65, "MAE_30D_pct": -5.49, "MAE_90D_pct": -5.49, "MAE_180D_pct": -5.49, "MAE_1Y_pct": -5.49, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-22", "peak_price": 346000, "drawdown_after_peak_pct": -13.58, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "same_entry_group_id": "R6L11-C22-000810-20230515-227500", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "corporate_action_window_status": "clean_180D_window", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "round": "R6", "loop": "11", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_IFRS17_CSM_RESERVE_QUALITY_CAPITAL_RETURN", "sector": "insurance_nonlife_financials", "primary_archetype": "IFRS17_CSM_ROE_reserve_quality_capital_return", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}

{"row_type": "trigger", "trigger_id": "R6L11-C22-000810-T2", "case_id": "R6L11-C22-000810-20230515", "symbol": "000810", "company_name": "삼성화재", "trigger_type": "Stage4B", "trigger_date": "2024-03-21", "entry_date": "2024-03-21", "entry_price": 343000, "evidence_available_at_that_date": "보험 value-up/capital-return 기대가 가격에 선반영되고 단기 위치가 과열된 구간. 가격만으로 full 4B 확정하지 않음.", "evidence_source": "stock_web_price_row_for_overlay; non_price_4B_confirmation_to_attach_later", "stage2_evidence_fields": [], "stage3_evidence_fields": ["financial_visibility"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000810/2024.csv", "profile_path": "atlas/symbol_profiles/000/000810.json", "MFE_30D_pct": 0.87, "MFE_90D_pct": 9.62, "MFE_180D_pct": 26.24, "MFE_1Y_pct": 80.18, "MFE_2Y_pct": 80.18, "MAE_30D_pct": -12.83, "MAE_90D_pct": -12.83, "MAE_180D_pct": -12.83, "MAE_1Y_pct": -12.83, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2026-02-20", "peak_price": 618000, "drawdown_after_peak_pct": 0.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.98, "four_b_full_window_peak_proximity": 0.43, "four_b_timing_verdict": "price_only_local_4B_too_early", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "4B_too_early", "current_profile_verdict": "current_profile_4B_too_early", "same_entry_group_id": "R6L11-C22-000810-20240321-343000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": "same_case_new_4B_path", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false, "corporate_action_window_status": "clean_180D_window", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "round": "R6", "loop": "11", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_IFRS17_CSM_RESERVE_QUALITY_CAPITAL_RETURN", "sector": "insurance_nonlife_financials", "primary_archetype": "IFRS17_CSM_ROE_reserve_quality_capital_return", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}

{"row_type": "trigger", "trigger_id": "R6L11-C22-005830-T1", "case_id": "R6L11-C22-005830-20230515", "symbol": "005830", "company_name": "DB손해보험", "trigger_type": "Stage2-Actionable", "trigger_date": "2023-05-12", "entry_date": "2023-05-15", "entry_price": 76200, "evidence_available_at_that_date": "IFRS17 이후 CSM/ROE/배당여력 재평가 가능성. 초기 90D는 흔들렸으나 180D에서 재평가 확인.", "evidence_source": "stock_web_price_only_plus_public_IFRS17_result_context__attach_DART_KRX_ids_later", "stage2_evidence_fields": ["public_event_or_disclosure", "early_revision_signal", "relative_strength"], "stage3_evidence_fields": ["financial_visibility", "confirmed_revision"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005830/2023.csv", "profile_path": "atlas/symbol_profiles/005/005830.json", "MFE_30D_pct": 9.58, "MFE_90D_pct": 8.53, "MFE_180D_pct": 38.32, "MFE_1Y_pct": 44.36, "MFE_2Y_pct": 152.36, "MAE_30D_pct": -3.41, "MAE_90D_pct": -7.48, "MAE_180D_pct": -7.48, "MAE_1Y_pct": -7.48, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-14", "peak_price": 110000, "drawdown_after_peak_pct": -15.36, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "missed_structural", "current_profile_verdict": "current_profile_too_late", "same_entry_group_id": "R6L11-C22-005830-20230515-76200", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "corporate_action_window_status": "clean_180D_window", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "round": "R6", "loop": "11", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_IFRS17_CSM_RESERVE_QUALITY_CAPITAL_RETURN", "sector": "insurance_nonlife_financials", "primary_archetype": "IFRS17_CSM_ROE_reserve_quality_capital_return", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}

{"row_type": "trigger", "trigger_id": "R6L11-C22-005830-T2", "case_id": "R6L11-C22-005830-20230515", "symbol": "005830", "company_name": "DB손해보험", "trigger_type": "Stage3-Green", "trigger_date": "2024-02-02", "entry_date": "2024-02-02", "entry_price": 99200, "evidence_available_at_that_date": "capital-return/value-up 테마와 손보 ROE 재평가가 뒤늦게 결합된 확인 구간.", "evidence_source": "stock_web_price_row_for_lateness_audit; attach_public_evidence_later", "stage2_evidence_fields": [], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005830/2024.csv", "profile_path": "atlas/symbol_profiles/005/005830.json", "MFE_30D_pct": 10.89, "MFE_90D_pct": 16.94, "MFE_180D_pct": 49.19, "MFE_1Y_pct": 93.85, "MFE_2Y_pct": 93.85, "MAE_30D_pct": -8.17, "MAE_90D_pct": -8.17, "MAE_180D_pct": -8.17, "MAE_1Y_pct": -8.17, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2026-02-20", "peak_price": 192300, "drawdown_after_peak_pct": 0.0, "green_lateness_ratio": 0.68, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "late_green_but_not_fatal", "current_profile_verdict": "current_profile_too_late", "same_entry_group_id": "R6L11-C22-005830-20240202-99200", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": true, "reuse_reason": "same_case_stage3_lateness_audit", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false, "corporate_action_window_status": "clean_180D_window", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "round": "R6", "loop": "11", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_IFRS17_CSM_RESERVE_QUALITY_CAPITAL_RETURN", "sector": "insurance_nonlife_financials", "primary_archetype": "IFRS17_CSM_ROE_reserve_quality_capital_return", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}

{"row_type": "trigger", "trigger_id": "R6L11-C22-001450-T1", "case_id": "R6L11-C22-001450-20230515", "symbol": "001450", "company_name": "현대해상", "trigger_type": "Stage2-Actionable_candidate_rejected", "trigger_date": "2023-05-12", "entry_date": "2023-05-15", "entry_price": 34750, "evidence_available_at_that_date": "IFRS17 basket signal은 있었으나 reserve/claim-ratio penalty가 함께 없으면 false positive가 됨.", "evidence_source": "stock_web_price_only_plus_public_IFRS17_result_context__attach_DART_KRX_ids_later", "stage2_evidence_fields": ["public_event_or_disclosure", "early_revision_signal"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001450/2023.csv", "profile_path": "atlas/symbol_profiles/001/001450.json", "MFE_30D_pct": 4.46, "MFE_90D_pct": 4.46, "MFE_180D_pct": 5.9, "MFE_1Y_pct": 5.9, "MFE_2Y_pct": 11.65, "MAE_30D_pct": -13.38, "MAE_90D_pct": -21.58, "MAE_180D_pct": -21.58, "MAE_1Y_pct": -21.58, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-05", "peak_price": 36800, "drawdown_after_peak_pct": -16.17, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "false_positive_green", "current_profile_verdict": "current_profile_false_positive", "same_entry_group_id": "R6L11-C22-001450-20230515-34750", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "corporate_action_window_status": "clean_180D_window", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "round": "R6", "loop": "11", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_IFRS17_CSM_RESERVE_QUALITY_CAPITAL_RETURN", "sector": "insurance_nonlife_financials", "primary_archetype": "IFRS17_CSM_ROE_reserve_quality_capital_return", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}

{"row_type": "trigger", "trigger_id": "R6L11-C22-000370-T1", "case_id": "R6L11-C22-000370-20230515", "symbol": "000370", "company_name": "한화손해보험", "trigger_type": "Stage2-Actionable_candidate_rejected", "trigger_date": "2023-05-12", "entry_date": "2023-05-15", "entry_price": 4380, "evidence_available_at_that_date": "중소형 손보 beta와 IFRS17 headline은 있었지만 capital-return visibility 부족과 높은 MAE가 핵심.", "evidence_source": "stock_web_price_only_plus_public_IFRS17_result_context__attach_DART_KRX_ids_later", "stage2_evidence_fields": ["public_event_or_disclosure", "relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000370/2023.csv", "profile_path": "atlas/symbol_profiles/000/000370.json", "MFE_30D_pct": 13.47, "MFE_90D_pct": 13.47, "MFE_180D_pct": 13.47, "MFE_1Y_pct": 38.81, "MFE_2Y_pct": 112.33, "MAE_30D_pct": -10.96, "MAE_90D_pct": -18.72, "MAE_180D_pct": -18.72, "MAE_1Y_pct": -18.72, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2026-02-20", "peak_price": 9300, "drawdown_after_peak_pct": 0.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "high_mae_success", "current_profile_verdict": "current_profile_false_positive", "same_entry_group_id": "R6L11-C22-000370-20230515-4380", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "corporate_action_window_status": "clean_180D_window", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "round": "R6", "loop": "11", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_IFRS17_CSM_RESERVE_QUALITY_CAPITAL_RETURN", "sector": "insurance_nonlife_financials", "primary_archetype": "IFRS17_CSM_ROE_reserve_quality_capital_return", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}

{"row_type": "trigger", "trigger_id": "R6L11-C22-000400-T1", "case_id": "R6L11-C22-000400-20240201", "symbol": "000400", "company_name": "롯데손해보험", "trigger_type": "Stage2-Actionable_candidate_rejected", "trigger_date": "2024-02-01", "entry_date": "2024-02-01", "entry_price": 2610, "evidence_available_at_that_date": "거래량과 가격은 폭발했지만 C22의 reserve/CSM/capital-return 개선 evidence가 아니라 event-premium 성격.", "evidence_source": "stock_web_price_row_for_price_only_event; attach_news_or_disclosure_later", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["valuation_blowoff", "control_premium_or_event_premium", "price_only_local_peak"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000400/2024.csv", "profile_path": "atlas/symbol_profiles/000/000400.json", "MFE_30D_pct": 40.61, "MFE_90D_pct": 40.61, "MFE_180D_pct": 40.61, "MFE_1Y_pct": 40.61, "MFE_2Y_pct": 40.61, "MAE_30D_pct": -4.6, "MAE_90D_pct": -4.6, "MAE_180D_pct": -23.87, "MAE_1Y_pct": -23.87, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-16", "peak_price": 3670, "drawdown_after_peak_pct": -45.86, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.72, "four_b_full_window_peak_proximity": 0.72, "four_b_timing_verdict": "good_local_4B_but_not_positive_stage", "four_b_evidence_type": ["price_only", "control_premium_or_event_premium", "valuation_blowoff"], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "price_moved_without_evidence", "current_profile_verdict": "current_profile_correct", "same_entry_group_id": "R6L11-C22-000400-20240201-2610", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false, "corporate_action_window_status": "clean_180D_window", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "round": "R6", "loop": "11", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_IFRS17_CSM_RESERVE_QUALITY_CAPITAL_RETURN", "sector": "insurance_nonlife_financials", "primary_archetype": "IFRS17_CSM_ROE_reserve_quality_capital_return", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}

{"row_type": "trigger", "trigger_id": "R6L11-C22-000400-T2", "case_id": "R6L11-C22-000400-20240201", "symbol": "000400", "company_name": "롯데손해보험", "trigger_type": "Stage4C", "trigger_date": "2024-10-08", "entry_date": "2024-10-08", "entry_price": 2235, "evidence_available_at_that_date": "event-premium이 사라지고 구조적 C22 증거가 따라오지 않은 구간의 thesis-break protection row.", "evidence_source": "stock_web_price_row_for_4C_protection; attach_news_or_disclosure_later", "stage2_evidence_fields": [], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["thesis_evidence_broken", "forced_liquidation_or_crash"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000400/2024.csv", "profile_path": "atlas/symbol_profiles/000/000400.json", "MFE_30D_pct": 6.71, "MFE_90D_pct": 13.42, "MFE_180D_pct": 17.45, "MFE_1Y_pct": 17.45, "MFE_2Y_pct": 17.45, "MAE_30D_pct": -11.1, "MAE_90D_pct": -11.1, "MAE_180D_pct": -11.1, "MAE_1Y_pct": -11.1, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-04-10", "peak_price": 2625, "drawdown_after_peak_pct": -8.95, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable", "four_b_evidence_type": [], "four_c_protection_label": "hard_4c_success", "trigger_outcome_label": "4C_success", "current_profile_verdict": "current_profile_correct", "same_entry_group_id": "R6L11-C22-000400-20241008-2235", "dedupe_for_aggregate": false, "aggregate_group_role": "4C_overlay_only", "is_new_independent_case": true, "reuse_reason": "same_case_new_4C_path", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": false, "corporate_action_window_status": "clean_180D_window", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "round": "R6", "loop": "11", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "fine_archetype_id": "INSURANCE_IFRS17_CSM_RESERVE_QUALITY_CAPITAL_RETURN", "sector": "insurance_nonlife_financials", "primary_archetype": "IFRS17_CSM_ROE_reserve_quality_capital_return", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|4C_thesis_break_timing_test|sector_specific_rule_discovery|canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20"}

```

### 25.4 score_simulation rows
```jsonl

{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C22_shadow", "case_id": "R6L11-C22-000810-20230515", "trigger_id": "R6L11-C22-000810-T1", "symbol": "000810", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 62, "relative_strength_score": 56, "customer_quality_score": 0, "policy_or_regulatory_score": 70, "valuation_repricing_score": 63, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 10, "reserve_quality_score": 72, "csm_growth_score": 74, "capital_return_visibility_score": 68, "claim_ratio_risk_score": 18}, "weighted_score_before": 84.0, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 66, "relative_strength_score": 58, "customer_quality_score": 0, "policy_or_regulatory_score": 70, "valuation_repricing_score": 65, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 8, "reserve_quality_score": 78, "csm_growth_score": 78, "capital_return_visibility_score": 75, "claim_ratio_risk_score": 16}, "weighted_score_after": 88.0, "stage_label_after": "Stage3-Green_candidate", "changed_components": ["reserve_quality_score", "csm_growth_score", "capital_return_visibility_score", "claim_ratio_risk_score"], "component_delta_explanation": "C22에서는 IFRS17 headline을 그대로 promotion하지 않고, CSM 성장·reserve quality·capital return visibility가 함께 있어야 가산한다. Claim-ratio/reserve red flag와 price-only event premium은 차감한다.", "MFE_90D_pct": 20.66, "MAE_90D_pct": -5.49, "score_return_alignment_label": "structural_success", "current_profile_verdict": "current_profile_correct"}

{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C22_shadow", "case_id": "R6L11-C22-000810-20230515", "trigger_id": "R6L11-C22-000810-T2", "symbol": "000810", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 82, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 88, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "reserve_quality_score": 78, "csm_growth_score": 0, "capital_return_visibility_score": 75, "claim_ratio_risk_score": 0, "positioning_overheat_score": 88}, "weighted_score_before": 92.0, "stage_label_before": "Stage4B_price_only_watch", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 0, "relative_strength_score": 82, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 88, "execution_risk_score": 25, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "reserve_quality_score": 78, "csm_growth_score": 0, "capital_return_visibility_score": 75, "claim_ratio_risk_score": 0, "positioning_overheat_score": 90}, "weighted_score_after": 90.0, "stage_label_after": "Stage4B_watch_not_full_exit", "changed_components": ["reserve_quality_score", "csm_growth_score", "capital_return_visibility_score", "claim_ratio_risk_score"], "component_delta_explanation": "C22에서는 IFRS17 headline을 그대로 promotion하지 않고, CSM 성장·reserve quality·capital return visibility가 함께 있어야 가산한다. Claim-ratio/reserve red flag와 price-only event premium은 차감한다.", "MFE_90D_pct": 9.62, "MAE_90D_pct": -12.83, "score_return_alignment_label": "4B_too_early", "current_profile_verdict": "current_profile_4B_too_early"}

{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C22_shadow", "case_id": "R6L11-C22-005830-20230515", "trigger_id": "R6L11-C22-005830-T1", "symbol": "005830", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 57, "relative_strength_score": 48, "customer_quality_score": 0, "policy_or_regulatory_score": 68, "valuation_repricing_score": 58, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "reserve_quality_score": 66, "csm_growth_score": 68, "capital_return_visibility_score": 60, "claim_ratio_risk_score": 24}, "weighted_score_before": 73.0, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 60, "relative_strength_score": 50, "customer_quality_score": 0, "policy_or_regulatory_score": 68, "valuation_repricing_score": 61, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "reserve_quality_score": 72, "csm_growth_score": 72, "capital_return_visibility_score": 66, "claim_ratio_risk_score": 22}, "weighted_score_after": 78.0, "stage_label_after": "Stage3-Yellow", "changed_components": ["reserve_quality_score", "csm_growth_score", "capital_return_visibility_score", "claim_ratio_risk_score"], "component_delta_explanation": "C22에서는 IFRS17 headline을 그대로 promotion하지 않고, CSM 성장·reserve quality·capital return visibility가 함께 있어야 가산한다. Claim-ratio/reserve red flag와 price-only event premium은 차감한다.", "MFE_90D_pct": 8.53, "MAE_90D_pct": -7.48, "score_return_alignment_label": "missed_structural", "current_profile_verdict": "current_profile_too_late"}

{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C22_shadow", "case_id": "R6L11-C22-005830-20230515", "trigger_id": "R6L11-C22-005830-T2", "symbol": "005830", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 68, "relative_strength_score": 67, "customer_quality_score": 0, "policy_or_regulatory_score": 72, "valuation_repricing_score": 70, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "reserve_quality_score": 75, "csm_growth_score": 74, "capital_return_visibility_score": 74, "claim_ratio_risk_score": 0}, "weighted_score_before": 88.0, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 68, "relative_strength_score": 67, "customer_quality_score": 0, "policy_or_regulatory_score": 72, "valuation_repricing_score": 70, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "reserve_quality_score": 75, "csm_growth_score": 74, "capital_return_visibility_score": 74, "claim_ratio_risk_score": 0}, "weighted_score_after": 88.0, "stage_label_after": "Stage3-Green", "changed_components": ["reserve_quality_score", "csm_growth_score", "capital_return_visibility_score", "claim_ratio_risk_score"], "component_delta_explanation": "C22에서는 IFRS17 headline을 그대로 promotion하지 않고, CSM 성장·reserve quality·capital return visibility가 함께 있어야 가산한다. Claim-ratio/reserve red flag와 price-only event premium은 차감한다.", "MFE_90D_pct": 16.94, "MAE_90D_pct": -8.17, "score_return_alignment_label": "late_green_but_not_fatal", "current_profile_verdict": "current_profile_too_late"}

{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C22_shadow", "case_id": "R6L11-C22-001450-20230515", "trigger_id": "R6L11-C22-001450-T1", "symbol": "001450", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 55, "relative_strength_score": 42, "customer_quality_score": 0, "policy_or_regulatory_score": 68, "valuation_repricing_score": 55, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "reserve_quality_score": 45, "csm_growth_score": 58, "capital_return_visibility_score": 50, "claim_ratio_risk_score": 55}, "weighted_score_before": 76.0, "stage_label_before": "Stage3-Yellow_false_positive_risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 50, "relative_strength_score": 35, "customer_quality_score": 0, "policy_or_regulatory_score": 68, "valuation_repricing_score": 48, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "reserve_quality_score": 38, "csm_growth_score": 54, "capital_return_visibility_score": 44, "claim_ratio_risk_score": 72}, "weighted_score_after": 64.0, "stage_label_after": "Stage2_watch_or_reject", "changed_components": ["reserve_quality_score", "csm_growth_score", "capital_return_visibility_score", "claim_ratio_risk_score"], "component_delta_explanation": "C22에서는 IFRS17 headline을 그대로 promotion하지 않고, CSM 성장·reserve quality·capital return visibility가 함께 있어야 가산한다. Claim-ratio/reserve red flag와 price-only event premium은 차감한다.", "MFE_90D_pct": 4.46, "MAE_90D_pct": -21.58, "score_return_alignment_label": "false_positive_green", "current_profile_verdict": "current_profile_false_positive"}

{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C22_shadow", "case_id": "R6L11-C22-000370-20230515", "trigger_id": "R6L11-C22-000370-T1", "symbol": "000370", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 50, "relative_strength_score": 45, "customer_quality_score": 0, "policy_or_regulatory_score": 68, "valuation_repricing_score": 54, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "reserve_quality_score": 42, "csm_growth_score": 54, "capital_return_visibility_score": 34, "claim_ratio_risk_score": 62}, "weighted_score_before": 74.0, "stage_label_before": "Stage2-Actionable_false_positive_risk", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 47, "relative_strength_score": 42, "customer_quality_score": 0, "policy_or_regulatory_score": 68, "valuation_repricing_score": 50, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "reserve_quality_score": 36, "csm_growth_score": 50, "capital_return_visibility_score": 28, "claim_ratio_risk_score": 75}, "weighted_score_after": 59.0, "stage_label_after": "Stage2_watch_or_reject", "changed_components": ["reserve_quality_score", "csm_growth_score", "capital_return_visibility_score", "claim_ratio_risk_score"], "component_delta_explanation": "C22에서는 IFRS17 headline을 그대로 promotion하지 않고, CSM 성장·reserve quality·capital return visibility가 함께 있어야 가산한다. Claim-ratio/reserve red flag와 price-only event premium은 차감한다.", "MFE_90D_pct": 13.47, "MAE_90D_pct": -18.72, "score_return_alignment_label": "high_mae_success", "current_profile_verdict": "current_profile_false_positive"}

{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C22_shadow", "case_id": "R6L11-C22-000400-20240201", "trigger_id": "R6L11-C22-000400-T1", "symbol": "000400", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 30, "relative_strength_score": 85, "customer_quality_score": 0, "policy_or_regulatory_score": 45, "valuation_repricing_score": 82, "execution_risk_score": 0, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "reserve_quality_score": 25, "csm_growth_score": 30, "capital_return_visibility_score": 20, "claim_ratio_risk_score": 65}, "weighted_score_before": 78.0, "stage_label_before": "Stage3-Yellow_if_price_overweighted", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 25, "relative_strength_score": 70, "customer_quality_score": 0, "policy_or_regulatory_score": 45, "valuation_repricing_score": 55, "execution_risk_score": 0, "legal_or_contract_risk_score": 55, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "reserve_quality_score": 20, "csm_growth_score": 25, "capital_return_visibility_score": 18, "claim_ratio_risk_score": 75}, "weighted_score_after": 52.0, "stage_label_after": "Stage2_watch_or_4B_event_overlay_only", "changed_components": ["reserve_quality_score", "csm_growth_score", "capital_return_visibility_score", "claim_ratio_risk_score"], "component_delta_explanation": "C22에서는 IFRS17 headline을 그대로 promotion하지 않고, CSM 성장·reserve quality·capital return visibility가 함께 있어야 가산한다. Claim-ratio/reserve red flag와 price-only event premium은 차감한다.", "MFE_90D_pct": 40.61, "MAE_90D_pct": -4.6, "score_return_alignment_label": "price_moved_without_evidence", "current_profile_verdict": "current_profile_correct"}

{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy_to_C22_shadow", "case_id": "R6L11-C22-000400-20240201", "trigger_id": "R6L11-C22-000400-T2", "symbol": "000400", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 20, "relative_strength_score": 25, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 30, "execution_risk_score": 0, "legal_or_contract_risk_score": 70, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "reserve_quality_score": 15, "csm_growth_score": 15, "capital_return_visibility_score": 10, "claim_ratio_risk_score": 80}, "weighted_score_before": 36.0, "stage_label_before": "Stage4C", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 20, "relative_strength_score": 25, "customer_quality_score": 0, "policy_or_regulatory_score": 0, "valuation_repricing_score": 30, "execution_risk_score": 0, "legal_or_contract_risk_score": 70, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0, "reserve_quality_score": 15, "csm_growth_score": 15, "capital_return_visibility_score": 10, "claim_ratio_risk_score": 80}, "weighted_score_after": 36.0, "stage_label_after": "Stage4C", "changed_components": ["reserve_quality_score", "csm_growth_score", "capital_return_visibility_score", "claim_ratio_risk_score"], "component_delta_explanation": "C22에서는 IFRS17 headline을 그대로 promotion하지 않고, CSM 성장·reserve quality·capital return visibility가 함께 있어야 가산한다. Claim-ratio/reserve red flag와 price-only event premium은 차감한다.", "MFE_90D_pct": 13.42, "MAE_90D_pct": -11.1, "score_return_alignment_label": "4C_success", "current_profile_verdict": "current_profile_correct"}

```

### 25.5 shadow_weight rows
```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,c22_reserve_quality_gate,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"Do not promote generic IFRS17 headline without reserve-quality and claim-ratio check","Hyundai/Hanwha false positives blocked while Samsung/DB remain eligible","R6L11-C22-001450-T1|R6L11-C22-000370-T1|R6L11-C22-000810-T1|R6L11-C22-005830-T1",5,5,3,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c22_capital_return_visibility_bonus,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,0,1,+1,"CSM/ROE plus capital-return visibility separates clean rerating from accounting-only signal","Samsung/DB 180D MFE remained positive after early evidence","R6L11-C22-000810-T1|R6L11-C22-005830-T1",2,2,0,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,c22_price_only_event_premium_block,canonical_archetype_specific,L6_FINANCIAL_CAPITAL_RETURN_DIGITAL,C22_INSURANCE_RATE_CYCLE_RESERVE,1,1,0,"Existing price-only blowoff guard is kept and specialized for insurance M&A/event premium","Lotte price spike had high local MFE but poor full-window alignment","R6L11-C22-000400-T1|R6L11-C22-000400-T2",1,1,1,medium,axis_stress_test,"strengthens existing axis; no new global delta"
```

### 25.6 residual_contribution row
```jsonl
{"row_type": "residual_contribution", "round": "R6", "loop": "11", "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "scheduled_round": "R6", "scheduled_loop": 11, "round_schedule_status": "valid", "round_sector_consistency": "pass", "new_independent_case_count": 5, "reused_case_count": 0, "new_symbol_count": 5, "same_archetype_new_symbol_count": 5, "same_archetype_new_trigger_family_count": 5, "new_trigger_family_count": 5, "positive_case_count": 2, "counterexample_count": 3, "current_profile_error_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_yellow_total_min", "stage3_green_total_min", "stage3_green_revision_min", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["generic_IFRS17_false_positive", "reserve_claim_ratio_penalty_missing", "capital_return_visibility_delayed", "price_only_event_premium_local_MFE"], "diversity_score_summary": "new_symbols=5; new_trigger_families=5; counterexamples=3; residual_errors=3; wrong_round_penalty=0", "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

### 25.7 narrative_only rows
```jsonl

{"row_type": "narrative_only", "case_id": "none", "symbol": null, "large_sector_id": "L6_FINANCIAL_CAPITAL_RETURN_DIGITAL", "canonical_archetype_id": "C22_INSURANCE_RATE_CYCLE_RESERVE", "reason": "all selected cases have stock_web_forward_180D_window_available", "price_source": "Songdaiki/stock-web", "usage": "not_weight_calibration"}

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
completed_round = R6
completed_loop = 11
next_round = R7
next_loop = 11
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- stock_agent R6 coverage artifact: representative_triggers=101, unique_cases=25, and trigger distribution read from `reports/e2r_calibration/by_round/R6.md`.

- stock-web manifest: `atlas/manifest.json`; max_date `2026-02-20`; tradable shard root `atlas/ohlcv_tradable_by_symbol_year`; raw/unadjusted caveat.

- Profiles checked: `000810`, `005830`, `001450`, `000370`, `000400`; old corporate-action candidate dates do not overlap tested 2023-2024 180D windows.

- OHLC rows inspected: Samsung Fire 2023-05 and 2024-02/03; DB Insurance 2023-05/08 and 2024-01/03; Hyundai Marine 2023-05/07 and 2024-01/03; Hanwha General 2023-05/08; Lotte Non-Life 2024-02 and 2024-08/11.

- Exact event evidence IDs are intentionally deferred; this MD should not be promoted to production without attaching DART/KIND/news/report identifiers.

