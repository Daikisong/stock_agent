# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```yaml
research_session: post_calibrated_sector_archetype_residual_research
mode: historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12
output_file: e2r_stock_web_v12_residual_round_R2_loop_15_L2_AI_SEMICONDUCTOR_ELECTRONICS_C06_HBM_MEMORY_CUSTOMER_CAPACITY_research.md
scheduled_round: R2
scheduled_loop: 15
completed_round: R2
completed_loop: 15
next_round: R3
next_loop: 15
round_schedule_status: valid
round_sector_consistency: pass
large_sector_id: L2_AI_SEMICONDUCTOR_ELECTRONICS
canonical_archetype_id: C06_HBM_MEMORY_CUSTOMER_CAPACITY
fine_archetype_id: HBM_CUSTOMER_CAPACITY_DIRECTNESS_GATE
production_scoring_changed: false
shadow_weight_only: true
handoff_prompt_embedded: true
handoff_prompt_executed_now: false
```

This loop adds 3 new independent cases, 1 counterexamples, and 2 residual errors for R2/L2_AI_SEMICONDUCTOR_ELECTRONICS/C06_HBM_MEMORY_CUSTOMER_CAPACITY.

## 1. Current Calibrated Profile Assumption

Current default proxy is `e2r_2_1_stock_web_calibrated_proxy`; rollback reference is `e2r_2_0_baseline_reference`.

Already-applied global axes are kept as production assumptions: Stage2 actionable bonus +2.0, Yellow total min 75, Green total min 87, Green revision min 55, cross-evidence Green buffer +1.5, price-only blowoff blocks positive promotion, full 4B requires non-price evidence, and hard 4C thesis-break routing.

This MD does not patch `stock_agent`, does not open `src/e2r`, and does not scan current candidates.

## 2. Round / Large Sector / Canonical Archetype Scope

- Round: R2
- Large sector: L2_AI_SEMICONDUCTOR_ELECTRONICS
- Canonical archetype: C06_HBM_MEMORY_CUSTOMER_CAPACITY
- Fine archetype: HBM_CUSTOMER_CAPACITY_DIRECTNESS_GATE
- Objective: C06-specific residual separation between direct HBM customer/capacity evidence, generic memory recovery narrative, Green timing, and price-only 4B watch overlay.

## 3. Previous Coverage / Duplicate Avoidance Check

Allowed research artifacts showed prior broad calibration coverage through R1~R13 and loops 1~9 in ingested historical files, with global axes already applied. The immediately prior conversational state completed R1 Loop 15 and set next_round=R2 / next_loop=15. Therefore this file is R2 Loop 15.

Duplicate-avoidance stance:

- Do not repeat generic “Stage2 is earlier than Green.”
- Do not re-prove the already-applied full-4B non-price guard.
- Use C06 to separate **direct HBM customer/capacity evidence** from **generic memory recovery**.
- Same SK하이닉스 symbol is reused only for a distinct 4B overlay trigger family.

## 4. Stock-Web OHLC Input / Price Source Validation

Manifest fields verified:

```json
{
  "source_name": "FinanceData/marcap",
  "source_repo_url": "https://github.com/FinanceData/marcap",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "min_date": "1995-05-02",
  "max_date": "2026-02-20",
  "raw_row_count": 15214118,
  "tradable_row_count": 14354401,
  "symbol_count": 5414,
  "active_like_symbol_count": 2868,
  "inactive_or_delisted_like_symbol_count": 2546,
  "markets": [
    "KONEX",
    "KOSDAQ",
    "KOSDAQ GLOBAL",
    "KOSPI"
  ],
  "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year",
  "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year",
  "schema_path": "atlas/schema.json",
  "universe_path": "atlas/universe/all_symbols.csv"
}
```

Schema basis:

- Tradable columns: `d,o,h,l,c,v,a,mc,s,m`
- Raw columns: `d,o,h,l,c,v,a,mc,s,m,rs`
- Calibration basis: `tradable_raw`
- Price adjustment status: `raw_unadjusted_marcap`
- 180D quantitative calibration requires entry row, positive OHLCV, >=180 forward tradable days, computed MFE/MAE, and clean 180D corporate-action window.

## 5. Historical Eligibility Gate

All representative and overlay rows below use `Songdaiki/stock-web` tradable shards. 000660 and 005930 have 180D forward windows available. Profile-level corporate-action candidates are historical and do not overlap the 2024 entry-to-180D windows used here.

## 6. Canonical Archetype Compression Map

| fine_archetype_id | canonical_archetype_id | compression logic |
|---|---|---|
| HBM_CUSTOMER_CAPACITY_DIRECTNESS_GATE | C06_HBM_MEMORY_CUSTOMER_CAPACITY | Direct customer/capacity proof, capacity bookedness, and qualification route matter more than generic memory-cycle recovery. |
| HBM_PRICE_ONLY_4B_WATCH_OVERLAY | C06_HBM_MEMORY_CUSTOMER_CAPACITY | Price-only blowoff remains blocked from full 4B but can be stored as a C06 watch overlay after extreme rerating. |

## 7. Case Selection Summary

| case_id | symbol | company | case_type | role | best_trigger | current_profile_verdict | independent_weight |
|---|---|---|---|---|---|---|---|
| R2L15_C06_000660_DIRECT_HBM_CAPACITY_SUCCESS | 000660 | SK하이닉스 | structural_success | positive | R2L15_C06_000660_STAGE2A_2024-01-25 | current_profile_correct | 1.0 |
| R2L15_C06_005930_GENERIC_MEMORY_HBM_LAG_COUNTER | 005930 | 삼성전자 | failed_rerating | counterexample | R2L15_C06_005930_COUNTER_2024-01-02 | current_profile_false_positive | 1.0 |
| R2L15_C06_000660_PRICE_ONLY_LOCAL_4B_WATCH | 000660 | SK하이닉스 | 4B_overlay_success | risk_overlay | R2L15_C06_000660_4B_PRICE_ONLY_2024-07-11 | current_profile_4B_too_late | 0.5 |

## 8. Positive vs Counterexample Balance

- Positive structural success: 1
- Counterexample / failed rerating: 1
- 4B overlay case: 1
- Calibration-usable cases: 3
- Calibration-usable triggers: 4

The balance is sufficient for a low-to-medium confidence C06-specific shadow rule candidate, not a global rule.

## 9. Evidence Source Map

| evidence family | SK하이닉스 | 삼성전자 |
|---|---|---|
| Direct HBM customer/capacity | HBM3E mass production / Nvidia shipment coverage; HBM products reported sold out for 2024 and nearly full for 2025 | Not yet confirmed at the early trigger; later Reuters qualification issue supports caution |
| Generic memory recovery | Present, but not the main positive driver | Present, but insufficient for C06 positive promotion |
| Green confirmation | May 2024 sold-out / capacity-booked evidence | No clean same-window Green trigger |
| 4B/4C | July 2024 price-only local peak validated watch overlay | HBM qualification issue is a 4C watch input, not positive evidence |

## 10. Price Data Source Map

| symbol | company | price_shard_path | profile_path | corporate_action_window_status |
|---|---|---|---|---|
| 000660 | SK하이닉스 | atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv | atlas/symbol_profiles/000/000660.json | clean_180D_window; profile corporate-action candidates are historical 1998-2003 only |
| 000660 | SK하이닉스 | atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv | atlas/symbol_profiles/000/000660.json | clean_180D_window |
| 005930 | 삼성전자 | atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv | atlas/symbol_profiles/005/005930.json | clean_180D_window; profile corporate-action candidates are historical 1996/1997/2018 only |
| 000660 | SK하이닉스 | atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv | atlas/symbol_profiles/000/000660.json | clean_180D_window |

## 11. Case-by-Case Trigger Grid

| trigger_id | symbol | trigger_type | trigger_date | entry_date | entry_price | MFE30 | MFE90 | MFE180 | MAE30 | MAE90 | MAE180 | current_profile_verdict | role |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R2L15_C06_000660_STAGE2A_2024-01-25 | 000660 | Stage2-Actionable | 2024-01-25 | 2024-01-26 | 136000 | 28.6 | 58.82 | 82.72 | -3.16 | -3.16 | -3.16 | current_profile_correct | representative |
| R2L15_C06_000660_GREEN_2024-05-02 | 000660 | Stage3-Green | 2024-05-02 | 2024-05-03 | 173200 | 35.39 | 43.48 | 43.48 | -2.42 | -13.11 | -16.46 | current_profile_correct | label_comparison_only |
| R2L15_C06_005930_COUNTER_2024-01-02 | 005930 | Stage2-Watch | 2024-01-02 | 2024-01-03 | 77000 | 2.34 | 11.69 | 15.32 | -8.18 | -8.18 | -19.22 | current_profile_false_positive | representative |
| R2L15_C06_000660_4B_PRICE_ONLY_2024-07-11 | 000660 | Stage4B-Watch | 2024-07-11 | 2024-07-11 | 241000 | 3.11 | 3.11 | 3.11 | -37.1 | -39.96 | -39.96 | current_profile_4B_too_late | 4B_overlay_only |

## 12. Trigger-Level OHLC Backtest Tables

| trigger_id | entry | 30D | 90D | 180D | 1Y | 2Y | peak |
|---|---:|---:|---:|---:|---:|---:|---|
| R2L15_C06_000660_STAGE2A_2024-01-25 | 136000 | +28.60 / -3.16 | +58.82 / -3.16 | +82.72 / -3.16 | +82.72 / -3.16 | +602.21 / -3.16 | 2026-02-20 high 955000 |
| R2L15_C06_000660_GREEN_2024-05-02 | 173200 | +35.39 / -2.42 | +43.48 / -13.11 | +43.48 / -16.46 | +451.39 / -16.46 | unavailable | 2026-02-20 high 955000 |
| R2L15_C06_005930_COUNTER_2024-01-02 | 77000 | +2.34 / -8.18 | +11.69 / -8.18 | +15.32 / -19.22 | +15.32 / -35.19 | +116.36 / -35.19 | 2026-01-29 high 166600 |
| R2L15_C06_000660_4B_PRICE_ONLY_2024-07-11 | 241000 | +3.11 / -37.10 | +3.11 / -39.96 | +3.11 / -39.96 | overlay-only | unavailable | 2024-07-11 high 248500 |

## 13. Current Calibrated Profile Stress Test

1. SK하이닉스 Stage2-Actionable was correctly captured as structural because the route had customer/capacity evidence beyond generic memory recovery.
2. 삼성전자 early-2024 generic HBM/memory recovery would be over-promoted if C06 did not require direct customer qualification or booked capacity.
3. Yellow threshold 75 is adequate, but C06 needs a component-level directness guard.
4. Green threshold 87 / revision 55 is kept; SK하이닉스 Green after May confirmation was not overly late.
5. Price-only blowoff remains blocked from positive stage promotion.
6. Full 4B non-price requirement is kept, but C06 needs a separate price-only watch overlay because the July 2024 SK하이닉스 drawdown was severe despite no hard thesis break.
7. Hard 4C routing should remain reserved for qualification failure, thesis break, or customer loss.

## 14. Stage2 / Yellow / Green Comparison

For SK하이닉스, Stage2-Actionable entry was 136000 on 2024-01-26. Green confirmation entry was 173200 on 2024-05-03. The observed full-window peak used for the Stage2 path was 248500 in the 180D window.

```text
green_lateness_ratio = (173200 - 136000) / (248500 - 136000) = 0.33
```

Interpretation: Green was somewhat later than Stage2, but not disastrously late. This supports keeping strict Green gates while improving C06-specific Stage2/Yellow evidence directness.

## 15. 4B Local vs Full-window Timing Audit

For the 2024-07-11 SK하이닉스 local high:

```text
four_b_local_peak_proximity = 1.00
four_b_full_window_peak_proximity = 0.10
four_b_timing_verdict = price_only_local_4B_too_early_for_full_window_but_valid_watch_overlay
```

The local drawdown after the July high was severe enough to validate risk monitoring. However, because the HBM thesis was not broken, this row should not train a full 4B exit rule. It should train only a C06 watch overlay.

## 16. 4C Protection Audit

Samsung’s later HBM qualification concern is a `thesis_break_watch_only` input for C06. It should not be used to train positive entry weights. SK하이닉스 July 2024 drawdown is not 4C because the direct HBM customer-capacity thesis remained intact.

## 17. Sector-Specific Rule Candidate

`L2_AI_SEMICONDUCTOR_ELECTRONICS` candidate:

> In AI/HBM memory, a broad “memory recovery” score should be capped below Stage3-Yellow unless the evidence includes direct customer qualification, booked HBM capacity, or delivery visibility. Otherwise large-cap memory names can be over-scored from theme heat alone.

Scope: sector_specific  
Confidence: medium-low  
Production action now: none; shadow ledger only.

## 18. Canonical-Archetype Rule Candidate

`C06_HBM_MEMORY_CUSTOMER_CAPACITY` candidate:

1. Add `C06_direct_customer_capacity_quality_gate`.
2. Add `C06_price_only_extreme_runup_4B_watch_overlay`.

The first is a positive/counterexample separator. The second is a risk overlay that explicitly does **not** weaken the existing full-4B non-price requirement.

## 19. Before / After Backtest Comparison

| profile | profile_id | scope | hypothesis | changed_axes | eligible | avg_MFE90 | avg_MAE90 | avg_MFE180 | avg_MAE180 | false_positive_rate | missed_structural | late_green | avg_green_lateness | 4B_local | 4B_full | verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| P0 | e2r_2_1_stock_web_calibrated_proxy | global current | current post-calibrated global gates only | none | 2 | 35.26 | -5.67 | 49.02 | -11.19 | 0.5 | 0 | 0 | 0.33 | None | None | mixed: positive captured but Samsung over-scored |
| P0b | e2r_2_0_baseline_reference | rollback | looser Green and no direct C06 guard | old thresholds | 2 | 35.26 | -5.67 | 49.02 | -11.19 | 0.5 | 0 | 1 | 0.33 | None | None | worse false-positive control |
| P1 | sector_specific_candidate_profile | L2 sector shadow | AI/HBM direct customer-capacity evidence matters more than generic memory recovery | +C06 customer_quality directness | 2 | 35.26 | -5.67 | 49.02 | -11.19 | 0.0 | 0 | 0 | 0.33 | None | None | better score-return alignment |
| P2 | canonical_archetype_candidate_profile | C06 canonical shadow | C06 needs direct qualification/capacity/booked evidence; price-only blowoff is watch overlay only | +customer gate; +4B watch overlay | 3 | 24.55 | -17.1 | 33.72 | -27.68 | 0.0 | 0 | 0 | 0.33 | 1.0 | 0.1 | best explanatory separation |
| P3 | counterexample_guard_profile | guard | generic AI-memory story without customer qualification stays below Yellow | Samsung guard | 2 | 35.26 | -5.67 | 49.02 | -11.19 | 0.0 | 0 | 0 | 0.33 | None | None | strong counterexample protection |

## 20. Score-Return Alignment Matrix

| case_id | before score/stage | after score/stage | return alignment |
|---|---|---|---|
| R2L15_C06_000660_DIRECT_HBM_CAPACITY_SUCCESS | 82 / Stage2-Actionable | 86 / Stage3-Yellow | Positive alignment improves without premature Green. |
| R2L15_C06_005930_GENERIC_MEMORY_HBM_LAG_COUNTER | 77 / Stage3-Yellow | 68 / Stage2-Watch | Counterexample fixed by directness guard. |
| R2L15_C06_000660_PRICE_ONLY_LOCAL_4B_WATCH | 91 / Stage3-Green | 79 / Stage4B-Watch | Drawdown risk captured without full 4B thesis-break. |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L2_AI_SEMICONDUCTOR_ELECTRONICS | C06_HBM_MEMORY_CUSTOMER_CAPACITY | HBM_CUSTOMER_CAPACITY_DIRECTNESS_GATE | 1 | 1 | 1 | 0 | 3 | 1 | 4 | 2 | 2 | true | true | Still needs more non-SKH/Samsung cases and one hard 4C qualification-failure row. |

## 22. Residual Contribution Summary

```yaml
new_independent_case_count: 3
reused_case_count: 1
reused_case_ids:
  - R2L15_C06_000660_PRICE_ONLY_LOCAL_4B_WATCH
new_symbol_count: 2
new_canonical_archetype_count: 1
new_fine_archetype_count: 2
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
residual_error_types_found:
  - generic_HBM_memory_false_positive
  - price_only_local_4B_watch_too_late
new_axis_proposed:
  - C06_direct_customer_capacity_quality_gate
  - C06_price_only_extreme_runup_4B_watch_overlay
existing_axis_strengthened:
  - full_4b_requires_non_price_evidence
existing_axis_weakened: null
existing_axis_kept:
  - stage3_green_revision_min
  - price_only_blowoff_blocks_positive_stage
sector_specific_rule_candidate: true
canonical_archetype_rule_candidate: true
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: false
```

## 23. Validation Scope / Non-Validation Scope

Validated:

- Historical OHLC from Songdaiki/stock-web.
- 30D/90D/180D MFE/MAE for all usable triggers.
- C06 distinction between direct customer/capacity evidence and generic recovery.
- 4B local vs full-window split.

Not validated:

- Live candidate discovery.
- Production scoring implementation.
- Brokerage or auto-trading logic.
- Full global rule promotion.

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C06_direct_customer_capacity_quality_gate,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"Generic memory recovery should not equal direct HBM customer/capacity evidence.","Reduced Samsung false-positive without blocking SK hynix structural success.","R2L15_C06_000660_STAGE2A_2024-01-25|R2L15_C06_005930_COUNTER_2024-01-02",2,2,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C06_price_only_extreme_runup_4B_watch_overlay,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"Price-only local peak is not full 4B but can flag drawdown risk in C06 after direct HBM thesis has rerated.","Captured July 2024 SK hynix drawdown watch without thesis-break routing.","R2L15_C06_000660_4B_PRICE_ONLY_2024-07-11",1,1,0,low,canonical_shadow_only,"watch overlay only; full_4b_requires_non_price_evidence remains kept"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R2L15_C06_000660_DIRECT_HBM_CAPACITY_SUCCESS", "symbol": "000660", "company_name": "SK하이닉스", "round": "R2", "loop": "15", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_CUSTOMER_CAPACITY_DIRECTNESS_GATE", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "R2L15_C06_000660_STAGE2A_2024-01-25", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "direct HBM customer/capacity evidence aligned with high MFE and shallow MAE", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Stage2-Actionable was enough; Green confirmation was not excessively late with lateness ratio 0.33."}
{"row_type": "case", "case_id": "R2L15_C06_005930_GENERIC_MEMORY_HBM_LAG_COUNTER", "symbol": "005930", "company_name": "삼성전자", "round": "R2", "loop": "15", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_CUSTOMER_CAPACITY_DIRECTNESS_GATE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "R2L15_C06_005930_COUNTER_2024-01-02", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "generic AI-memory narrative without customer qualification directness produced weak 180D MFE and high MAE", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Counterexample supports direct-customer qualification gate for C06."}
{"row_type": "case", "case_id": "R2L15_C06_000660_PRICE_ONLY_LOCAL_4B_WATCH", "symbol": "000660", "company_name": "SK하이닉스", "round": "R2", "loop": "15", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_CUSTOMER_CAPACITY_DIRECTNESS_GATE", "case_type": "4B_overlay_success", "positive_or_counterexample": "risk_overlay", "best_trigger": "R2L15_C06_000660_4B_PRICE_ONLY_2024-07-11", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": "same symbol as positive case but different 4B timing trigger family", "independent_evidence_weight": 0.5, "score_price_alignment": "price-only local peak captured severe drawdown risk but did not disprove full HBM thesis", "current_profile_verdict": "current_profile_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "Supports watch overlay, not full 4B."}
{"round": "R2", "loop": "15", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_CUSTOMER_CAPACITY_DIRECTNESS_GATE", "sector": "AI·반도체·전자부품", "primary_archetype": "HBM memory customer-capacity directness / supplier-quality separation", "loop_objective": "coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "row_type": "trigger", "trigger_id": "R2L15_C06_000660_STAGE2A_2024-01-25", "case_id": "R2L15_C06_000660_DIRECT_HBM_CAPACITY_SUCCESS", "symbol": "000660", "company_name": "SK하이닉스", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-25", "entry_date": "2024-01-26", "entry_price": 136000, "evidence_available_at_that_date": "Q4 2023 / 2024 outlook window already showed AI-memory and HBM demand as the core recovery route; subsequent March 2024 HBM3E mass production and May 2024 sold-out-capacity evidence confirms that this was not merely a generic memory rebound.", "evidence_source": "SK hynix earnings/outlook window; Reuters 2024-03-19 HBM3E mass production; WSJ 2024-05-02 HBM sold-out/backlog confirmation.", "stage2_evidence_fields": ["public_event_or_disclosure", "customer_or_order_quality", "capacity_or_volume_route", "early_revision_signal", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv", "profile_path": "atlas/symbol_profiles/000/000660.json", "MFE_30D_pct": 28.6, "MFE_90D_pct": 58.82, "MFE_180D_pct": 82.72, "MFE_1Y_pct": 82.72, "MFE_2Y_pct": 602.21, "MAE_30D_pct": -3.16, "MAE_90D_pct": -3.16, "MAE_180D_pct": -3.16, "MAE_1Y_pct": -3.16, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2026-02-20", "peak_price": 955000, "drawdown_after_peak_pct": 0.0, "green_lateness_ratio": 0.0, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_entry_trigger", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "structural_success", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; profile corporate-action candidates are historical 1998-2003 only", "same_entry_group_id": "R2L15_C06_000660_2024-01-26_136000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"round": "R2", "loop": "15", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_CUSTOMER_CAPACITY_DIRECTNESS_GATE", "sector": "AI·반도체·전자부품", "primary_archetype": "HBM memory customer-capacity directness / supplier-quality separation", "loop_objective": "coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "row_type": "trigger", "trigger_id": "R2L15_C06_000660_GREEN_2024-05-02", "case_id": "R2L15_C06_000660_DIRECT_HBM_CAPACITY_SUCCESS", "symbol": "000660", "company_name": "SK하이닉스", "trigger_type": "Stage3-Green", "trigger_date": "2024-05-02", "entry_date": "2024-05-03", "entry_price": 173200, "evidence_available_at_that_date": "HBM products were reported as sold out for 2024 and almost fully booked for 2025; this converted early HBM leadership into direct customer-capacity visibility.", "evidence_source": "WSJ 2024-05-02; Reuters March/April 2024 SK hynix HBM3E and advanced-packaging coverage.", "stage2_evidence_fields": ["customer_or_order_quality", "capacity_or_volume_route", "relative_strength"], "stage3_evidence_fields": ["confirmed_revision", "financial_visibility", "durable_customer_confirmation", "multiple_public_sources"], "stage4b_evidence_fields": [], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv", "profile_path": "atlas/symbol_profiles/000/000660.json", "MFE_30D_pct": 35.39, "MFE_90D_pct": 43.48, "MFE_180D_pct": 43.48, "MFE_1Y_pct": 451.39, "MFE_2Y_pct": null, "MAE_30D_pct": -2.42, "MAE_90D_pct": -13.11, "MAE_180D_pct": -16.46, "MAE_1Y_pct": -16.46, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2026-02-20", "peak_price": 955000, "drawdown_after_peak_pct": 0.0, "green_lateness_ratio": 0.33, "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_green_trigger", "four_b_evidence_type": [], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "green_not_too_late", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R2L15_C06_000660_2024-05-03_173200", "dedupe_for_aggregate": false, "aggregate_group_role": "label_comparison_only", "is_new_independent_case": false, "reuse_reason": "same symbol as Stage2 representative, but different trigger family for Green-lateness audit", "independent_evidence_weight": 0.25, "do_not_count_as_new_case": true}
{"round": "R2", "loop": "15", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_CUSTOMER_CAPACITY_DIRECTNESS_GATE", "sector": "AI·반도체·전자부품", "primary_archetype": "HBM memory customer-capacity directness / supplier-quality separation", "loop_objective": "coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "row_type": "trigger", "trigger_id": "R2L15_C06_005930_COUNTER_2024-01-02", "case_id": "R2L15_C06_005930_GENERIC_MEMORY_HBM_LAG_COUNTER", "symbol": "005930", "company_name": "삼성전자", "trigger_type": "Stage2-Watch", "trigger_date": "2024-01-02", "entry_date": "2024-01-03", "entry_price": 77000, "evidence_available_at_that_date": "Memory-cycle recovery and broad AI/HBM expectations were visible, but direct high-quality HBM3E customer qualification evidence was not yet confirmed. Later public reports on Nvidia qualification difficulty validated the need to separate generic memory recovery from direct HBM customer-capacity evidence.", "evidence_source": "Stock-Web selftest row for 005930; Reuters 2024-05-23 Samsung HBM qualification issue.", "stage2_evidence_fields": ["public_event_or_disclosure", "early_revision_signal"], "stage3_evidence_fields": [], "stage4b_evidence_fields": [], "stage4c_evidence_fields": ["qualification_failure", "thesis_evidence_broken"], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv", "profile_path": "atlas/symbol_profiles/005/005930.json", "MFE_30D_pct": 2.34, "MFE_90D_pct": 11.69, "MFE_180D_pct": 15.32, "MFE_1Y_pct": 15.32, "MFE_2Y_pct": 116.36, "MAE_30D_pct": -8.18, "MAE_90D_pct": -8.18, "MAE_180D_pct": -19.22, "MAE_1Y_pct": -35.19, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2026-01-29", "peak_price": 166600, "drawdown_after_peak_pct": 0.0, "green_lateness_ratio": "not_applicable:no_confirmed_Stage3_Green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_applicable_counterexample", "four_b_evidence_type": [], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "failed_rerating_near_term_hbm_counterexample", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window; profile corporate-action candidates are historical 1996/1997/2018 only", "same_entry_group_id": "R2L15_C06_005930_2024-01-03_77000", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"round": "R2", "loop": "15", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "fine_archetype_id": "HBM_CUSTOMER_CAPACITY_DIRECTNESS_GATE", "sector": "AI·반도체·전자부품", "primary_archetype": "HBM memory customer-capacity directness / supplier-quality separation", "loop_objective": "coverage_gap_fill|counterexample_mining|green_strictness_stress_test|4B_non_price_requirement_stress_test|canonical_archetype_compression", "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "row_type": "trigger", "trigger_id": "R2L15_C06_000660_4B_PRICE_ONLY_2024-07-11", "case_id": "R2L15_C06_000660_PRICE_ONLY_LOCAL_4B_WATCH", "symbol": "000660", "company_name": "SK하이닉스", "trigger_type": "Stage4B-Watch", "trigger_date": "2024-07-11", "entry_date": "2024-07-11", "entry_price": 241000, "evidence_available_at_that_date": "The stock had already repriced sharply into the July 2024 local high, but the available evidence was mainly price/positioning heat rather than non-price thesis break. The subsequent drawdown validates a watch overlay, not a full 4B unless non-price evidence appears.", "evidence_source": "Stock-Web 000660 2024 row around local high; no contemporaneous hard non-price break used for full 4B.", "stage2_evidence_fields": [], "stage3_evidence_fields": ["financial_visibility", "durable_customer_confirmation"], "stage4b_evidence_fields": ["valuation_blowoff", "positioning_overheat", "price_only_local_peak"], "stage4c_evidence_fields": [], "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv", "profile_path": "atlas/symbol_profiles/000/000660.json", "MFE_30D_pct": 3.11, "MFE_90D_pct": 3.11, "MFE_180D_pct": 3.11, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -37.1, "MAE_90D_pct": -39.96, "MAE_180D_pct": -39.96, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-11", "peak_price": 248500, "drawdown_after_peak_pct": -41.77, "green_lateness_ratio": "not_applicable:4B_overlay", "four_b_local_peak_proximity": 1.0, "four_b_full_window_peak_proximity": 0.1, "four_b_timing_verdict": "price_only_local_4B_too_early_for_full_window_but_valid_watch_overlay", "four_b_evidence_type": ["price_only", "valuation_blowoff", "positioning_overheat"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "4B_overlay_success_not_full_4B", "current_profile_verdict": "current_profile_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window", "same_entry_group_id": "R2L15_C06_000660_2024-07-11_241000", "dedupe_for_aggregate": false, "aggregate_group_role": "4B_overlay_only", "is_new_independent_case": true, "reuse_reason": "same symbol as positive case, but a distinct 4B price-only overlay trigger family", "independent_evidence_weight": 0.5, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R2L15_C06_000660_DIRECT_HBM_CAPACITY_SUCCESS", "trigger_id": "R2L15_C06_000660_STAGE2A_2024-01-25", "symbol": "000660", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 16, "relative_strength_score": 18, "customer_quality_score": 18, "policy_or_regulatory_score": 0, "valuation_repricing_score": 14, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 82, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 16, "relative_strength_score": 18, "customer_quality_score": 22, "policy_or_regulatory_score": 0, "valuation_repricing_score": 14, "execution_risk_score": -4, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 86, "stage_label_after": "Stage3-Yellow", "changed_components": ["customer_quality_score", "+C06_direct_customer_capacity_gate"], "component_delta_explanation": "Early HBM customer-capacity directness earns a C06-specific quality lift, but not automatic Green until direct booking/sold-out evidence appears.", "MFE_90D_pct": 58.82, "MAE_90D_pct": -3.16, "score_return_alignment_label": "aligned_positive", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "C06_direct_customer_capacity_guard_profile", "case_id": "R2L15_C06_005930_GENERIC_MEMORY_HBM_LAG_COUNTER", "trigger_id": "R2L15_C06_005930_COUNTER_2024-01-02", "symbol": "005930", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 14, "relative_strength_score": 6, "customer_quality_score": 10, "policy_or_regulatory_score": 0, "valuation_repricing_score": 16, "execution_risk_score": -2, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 77, "stage_label_before": "Stage3-Yellow", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 14, "relative_strength_score": 6, "customer_quality_score": 4, "policy_or_regulatory_score": 0, "valuation_repricing_score": 14, "execution_risk_score": -6, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 68, "stage_label_after": "Stage2-Watch", "changed_components": ["customer_quality_score", "execution_risk_score", "valuation_repricing_score"], "component_delta_explanation": "Generic memory-cycle recovery cannot substitute for direct HBM qualification/customer-capacity evidence under C06.", "MFE_90D_pct": 11.69, "MAE_90D_pct": -8.18, "score_return_alignment_label": "counterexample_fixed_by_guard", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "score_simulation", "profile_id": "C06_price_only_4B_watch_overlay_profile", "case_id": "R2L15_C06_000660_PRICE_ONLY_LOCAL_4B_WATCH", "trigger_id": "R2L15_C06_000660_4B_PRICE_ONLY_2024-07-11", "symbol": "000660", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "raw_component_scores_before": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 20, "relative_strength_score": 22, "customer_quality_score": 24, "policy_or_regulatory_score": 0, "valuation_repricing_score": 20, "execution_risk_score": -3, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 91, "stage_label_before": "Stage3-Green", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 20, "relative_strength_score": 22, "customer_quality_score": 24, "policy_or_regulatory_score": 0, "valuation_repricing_score": 20, "execution_risk_score": -12, "legal_or_contract_risk_score": 0, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 79, "stage_label_after": "Stage4B-Watch", "changed_components": ["execution_risk_score", "valuation_repricing_score", "positioning_overheat_score"], "component_delta_explanation": "Price-only blowoff still cannot become full 4B, but in C06 it should add a watch overlay after extreme runup because local drawdown risk was material.", "MFE_90D_pct": 3.11, "MAE_90D_pct": -39.96, "score_return_alignment_label": "watch_overlay_aligned", "current_profile_verdict": "current_profile_4B_too_late"}
{"row_type": "residual_contribution", "round": "R2", "loop": "15", "large_sector_id": "L2_AI_SEMICONDUCTOR_ELECTRONICS", "canonical_archetype_id": "C06_HBM_MEMORY_CUSTOMER_CAPACITY", "scheduled_round": "R2", "scheduled_loop": 15, "round_schedule_status": "valid", "round_sector_consistency": "pass", "new_independent_case_count": 3, "reused_case_count": 1, "new_symbol_count": 2, "same_archetype_new_symbol_count": 2, "same_archetype_new_trigger_family_count": 3, "new_trigger_family_count": 3, "positive_case_count": 1, "counterexample_count": 1, "current_profile_error_count": 2, "diversity_score_summary": "same_archetype_new_symbol +2; counterexample +1; new trigger families Stage2A/Green/4B; no wrong-round penalty", "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "stage3_green_revision_min", "full_4b_requires_non_price_evidence", "price_only_blowoff_blocks_positive_stage"], "residual_error_types_found": ["generic_HBM_memory_false_positive", "price_only_local_4B_watch_too_late"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": false}
```

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C06_direct_customer_capacity_quality_gate,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"Generic memory recovery should not equal direct HBM customer/capacity evidence.","Reduced Samsung false-positive without blocking SK hynix structural success.","R2L15_C06_000660_STAGE2A_2024-01-25|R2L15_C06_005930_COUNTER_2024-01-02",2,2,1,medium,canonical_shadow_only,"not production; post-calibrated residual"
shadow_weight,C06_price_only_extreme_runup_4B_watch_overlay,canonical_archetype_specific,L2_AI_SEMICONDUCTOR_ELECTRONICS,C06_HBM_MEMORY_CUSTOMER_CAPACITY,0,1,+1,"Price-only local peak is not full 4B but can flag drawdown risk in C06 after direct HBM thesis has rerated.","Captured July 2024 SK hynix drawdown watch without thesis-break routing.","R2L15_C06_000660_4B_PRICE_ONLY_2024-07-11",1,1,0,low,canonical_shadow_only,"watch overlay only; full_4b_requires_non_price_evidence remains kept"
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
completed_round = R2
completed_loop = 15
next_round = R3
next_loop = 15
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

- Songdaiki/stock-web `atlas/manifest.json`: max_date 2026-02-20; price basis tradable_raw; raw_unadjusted_marcap.
- Songdaiki/stock-web `atlas/schema.json`: MFE/MAE calculation and calibration usability rules.
- Songdaiki/stock-web `diagnostics/chatgpt_bundle.txt`: 005930 and 000660 selftest references.
- Songdaiki/stock-web `atlas/ohlcv_tradable_by_symbol_year/000/000660/2024.csv`, `2025.csv`, `2026.csv`.
- Songdaiki/stock-web `atlas/ohlcv_tradable_by_symbol_year/005/005930/2024.csv`.
- Historical evidence references used only for trigger context: Reuters 2024-03-19, WSJ 2024-05-02, Reuters 2024-05-23.
