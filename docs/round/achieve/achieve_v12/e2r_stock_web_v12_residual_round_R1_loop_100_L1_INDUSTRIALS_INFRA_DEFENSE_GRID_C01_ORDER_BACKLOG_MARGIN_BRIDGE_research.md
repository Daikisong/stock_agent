# E2R Stock-Web Historical Calibration / Sector-Archetype Residual Research Round

## 0. Research Metadata

```text
selected_round = R1
selected_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
large_sector_id = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE
fine_archetype_id = SHIPBUILDING_AND_MACHINERY_ORDER_BACKLOG_MARGIN_BRIDGE_VS_EQUIPMENT_BETA_NO_CASH_CONVERSION
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
price_source = Songdaiki/stock-web
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
stock_web_manifest_max_date = 2026-02-20
```

## 1. Current Calibrated Profile Assumption

- `before_profile_id`: `e2r_2_1_stock_web_calibrated_proxy`
- `after_profile_id`: `C01_order_backlog_margin_bridge_shadow_guard`
- `rollback_reference_profile_id`: `e2r_2_0_baseline_reference`
- This MD is **historical calibration research**, not live discovery.
- Non-price evidence is intentionally marked `source_proxy_only / evidence_url_pending=true`; therefore all patch rows are shadow-only.

## 2. Round / Large Sector / Canonical Archetype Scope

C01 is a L1 industrial archetype. The question is not “is the stock an industrial winner?” but:

> Did public order/backlog evidence connect to margin, delivery, and cash conversion before the price path rewarded it?

The useful split is:
- positive: backlog + delivery visibility + margin/revision bridge;
- counterexample: equipment/order vocabulary or sector beta without company-specific backlog/margin bridge;
- 4B overlay: valuation/positioning overheat after price has already rerated;
- 4C route: backlog or margin thesis break.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat Index says C01 has only 16 rows, still below the 30-row minimum stability band. This loop adds new C01 symbols and avoids the visible repeated C01 `082740` cluster.

- hard duplicate key avoided: `canonical_archetype_id + symbol + trigger_type + entry_date`
- new independent cases: 4
- reused cases: 0
- source limitation: source proxy only for non-price evidence

## 4. Stock-Web OHLC Input / Price Source Validation

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
```

## 5. Historical Eligibility Gate

All representative trigger rows below use:
- entry date present in Stock-Web tradable shard;
- positive OHLCV rows;
- 180 trading-day forward window available within manifest max date;
- no 2024-window corporate-action block detected from the symbol profile caveat fields used here.

## 6. Canonical Archetype Compression Map

| layer | value |
|---|---|
| large sector | L1_INDUSTRIALS_INFRA_DEFENSE_GRID |
| canonical | C01_ORDER_BACKLOG_MARGIN_BRIDGE |
| fine positive 1 | LARGE_SHIPBUILDING_BACKLOG_AND_MARGIN_CONVERSION |
| fine positive 2 | MID_SIZE_SHIP_ORDER_BACKLOG_MARGIN_TURNAROUND |
| fine positive 3 | SHIP_ENGINE_ORDER_BACKLOG_HIGH_MAE_SUCCESS |
| fine counterexample | CONSTRUCTION_MACHINERY_EQUIPMENT_BETA_NO_BACKLOG_MARGIN_BRIDGE |

## 7. Case Selection Summary

| case_id | symbol | company | role | entry | entry_price | MFE90 | MAE90 | verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| C01_R1L100_329180_shipbuilding_backlog_margin_bridge | 329180 | HD현대중공업 | structural_success | 2024-04-18 | 120300 | 84.95 | -6.48 | current_profile_correct |
| C01_R1L100_010620_midsize_ship_backlog_margin_bridge | 010620 | HD현대미포 | structural_success | 2024-04-18 | 64900 | 61.17 | -8.17 | current_profile_correct_but_green_late_risk |
| C01_R1L100_071970_ship_engine_backlog_high_mae_success | 071970 | HD현대마린엔진 | high_mae_success | 2024-04-18 | 13990 | 63.69 | -13.15 | current_profile_correct_with_high_mae_guardrail_needed |
| C01_R1L100_042670_machinery_beta_no_backlog_margin_bridge | 042670 | HD현대인프라코어 | failed_rerating | 2024-02-02 | 8400 | 3.69 | -13.21 | current_profile_false_positive_if_stage2_bonus_uses_equipment_beta_only |

## 8. Positive vs Counterexample Balance

- Positive structural success: 2
- High-MAE success: 1
- Counterexample / failed rerating: 1
- 4B / 4C path: watch-only overlays; no full 4B without non-price evidence

This is usable as a C01 residual loop but **not promotion-ready** because exact evidence URLs are pending.

## 9. Evidence Source Map

| symbol | evidence proxy | evidence_url_pending | calibration usage |
|---:|---|---|---|
| 329180 | large shipbuilding backlog + margin conversion narrative | true | representative positive |
| 010620 | mid-size ship order backlog + turnaround margin bridge | true | representative positive |
| 071970 | ship-engine backlog route, higher entry volatility | true | high-MAE positive guard |
| 042670 | construction machinery/equipment beta without fresh backlog margin bridge | true | counterexample |

## 10. Price Data Source Map

| symbol | price_shard_path | profile_path |
|---:|---|---|
| 329180 | `atlas/ohlcv_tradable_by_symbol_year/329/329180/2024.csv` | `atlas/symbol_profiles/329/329180.json` |
| 010620 | `atlas/ohlcv_tradable_by_symbol_year/010/010620/2024.csv` | `atlas/symbol_profiles/010/010620.json` |
| 071970 | `atlas/ohlcv_tradable_by_symbol_year/071/071970/2024.csv` | `atlas/symbol_profiles/071/071970.json` |
| 042670 | `atlas/ohlcv_tradable_by_symbol_year/042/042670/2024.csv` | `atlas/symbol_profiles/042/042670.json` |

## 11. Case-by-Case Trigger Grid

| symbol | trigger_type | stage2 evidence | stage3 evidence | 4B evidence | 4C evidence |
|---:|---|---|---|---|---|
| 329180 | Stage2-Actionable | public_order_backlog_visibility, relative_strength, backlog_or_delivery_visibility, early_revision_signal | confirmed_revision_proxy, margin_bridge_proxy, financial_visibility_proxy, low_red_team_risk | valuation_rerating_watch_after_80pct_mfe, positioning_overheat_watch | none |
| 010620 | Stage2-Actionable | public_order_backlog_visibility, relative_strength, backlog_or_delivery_visibility | margin_bridge_proxy, financial_visibility_proxy, repeat_order_or_conversion_proxy | valuation_blowoff_watch | none |
| 071970 | Stage2-Actionable | public_order_backlog_visibility, relative_strength, backlog_or_delivery_visibility | margin_bridge_proxy, durable_customer_confirmation_proxy | positioning_overheat_watch, valuation_blowoff_watch | none |
| 042670 | Stage2-FalsePositive-EquipmentBetaNoFreshBacklogMarginBridge | relative_strength | none | price_only_local_peak, margin_or_backlog_slowdown | thesis_evidence_broken |

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry_date | entry_price | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak_date | peak_price | drawdown_after_peak |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|
| 329180 | 2024-04-18 | 120300 | 21.36 | -6.48 | 84.95 | -6.48 | 84.95 | -6.48 | 2024-08-09 | 222500 | -22.56 |
| 010620 | 2024-04-18 | 64900 | 22.34 | -8.17 | 61.17 | -8.17 | 61.17 | -8.17 | 2024-07-17 | 104600 | -12.72 |
| 071970 | 2024-04-18 | 13990 | 27.23 | -8.15 | 63.69 | -13.15 | 63.69 | -13.15 | 2024-07-17 | 22900 | -15.07 |
| 042670 | 2024-02-02 | 8400 | 0.71 | -13.21 | 3.69 | -13.21 | 3.69 | -13.21 | 2024-03-28 | 8710 | -18.48 |

## 13. Current Calibrated Profile Stress Test

1. Current calibrated profile should accept Stage2 only if order/backlog evidence is paired with margin bridge.
2. HD현대중공업 and HD현대미포 support early Stage2-Actionable.
3. HD현대마린엔진 supports Stage2 but warns that high-MAE success needs entry guard.
4. HD현대인프라코어 shows the false-positive path: equipment beta without fresh backlog/margin bridge should not receive the same Stage2 bonus.
5. Green threshold 87 / revision 55 should stay unchanged.
6. Price-only blowoff should remain watch-only.
7. Full 4B requires non-price evidence.
8. Hard 4C should require thesis evidence break, not just a local peak.

## 14. Stage2 / Yellow / Green Comparison

C01 Stage2 is useful when it catches the backlog-to-margin bridge before the public Green label. But the counterexample shows why Stage2 cannot be “industrial sector strength + price action.” The bridge must contain at least two of:

- company-specific backlog/order visibility;
- delivery or utilization visibility;
- margin bridge / cost pass-through;
- early revision or OPM proxy;
- low execution-risk signal.

## 15. 4B Local vs Full-window Timing Audit

- 329180: price ran strongly after Stage2, but local peaks alone are not full 4B.
- 010620: Green would likely be late relative to Stage2; 4B is only watch until valuation/non-price overheat appears.
- 071970: high-MAE success; use 4B watch after strong MFE, not before thesis confirmation.
- 042670: price-only beta with weak bridge is not a 4B success; it is a Stage2 false positive / 4C watch.

## 16. 4C Protection Audit

Only 042670 receives a 4C-style thesis-break watch because backlog and margin evidence were not confirmed. Positive shipbuilding cases do not get hard 4C labels.

## 17. Sector-Specific Rule Candidate

No global delta proposed.

Sector/canonical shadow candidate:

```text
C01 Stage2-Actionable requires backlog_or_delivery_visibility AND margin_bridge_proxy.
Relative strength alone is insufficient.
```

## 18. Canonical-Archetype Rule Candidate

```text
C01_ORDER_BACKLOG_MARGIN_BRIDGE:
  promote Stage2 only when backlog visibility and margin bridge coexist.
  demote equipment/industrial beta with no company-specific backlog margin bridge.
  keep high-MAE success as Stage2/Yellow guard, not Green unlock.
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false positive count | missed structural count | verdict |
|---|---:|---:|---:|---:|---:|---|
| P0 e2r_2_1 proxy | 4 | 53.38 | -10.75 | 1 | 0 | too permissive if equipment beta counted |
| P2 C01 guard profile | 4 | 69.94 on accepted positives | -9.27 on accepted positives | 0 | 0 | better alignment, but source URL pending |

## 20. Score-Return Alignment Matrix

| symbol | score-return alignment |
|---:|---|
| 329180 | backlog/margin bridge aligned with high MFE |
| 010620 | backlog/margin bridge aligned with high MFE, Green could lag |
| 071970 | high-MAE success; entry guard needed |
| 042670 | equipment beta without bridge misaligns with return path |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive_case_count | counterexample_count | 4B_case_count | 4C_case_count | new_independent_case_count | reused_case_count | calibration_usable_trigger_count | representative_trigger_count | current_profile_error_count | sector_rule_candidate | canonical_rule_candidate | coverage_gap_after_this_loop |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C01_ORDER_BACKLOG_MARGIN_BRIDGE | SHIPBUILDING_AND_MACHINERY_ORDER_BACKLOG_MARGIN_BRIDGE_VS_EQUIPMENT_BETA_NO_CASH_CONVERSION | 3 | 1 | 0 | 1 watch | 4 | 0 | 4 | 4 | 1 | none | C01 backlog+margin bridge required | C01 remains below 30-row minimum stability band |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 4
new_trigger_family_count: 2
tested_existing_calibrated_axes:
- stage2_actionable_evidence_bonus
- full_4b_requires_non_price_evidence
- hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
- equipment_beta_without_backlog_margin_bridge_false_positive
- high_mae_success_requires_entry_guard
new_axis_proposed: false
existing_axis_strengthened: false
existing_axis_weakened: false
existing_axis_kept: true
sector_specific_rule_candidate: false
canonical_archetype_rule_candidate: true
no_new_signal_reason: not_applicable
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 4 new independent cases, 1 counterexamples, and 1 residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C01_ORDER_BACKLOG_MARGIN_BRIDGE.

## 23. Validation Scope / Non-Validation Scope

Validation scope:
- Stock-Web OHLC path;
- entry/peak/MFE/MAE arithmetic;
- duplicate-avoidance against visible index snapshot.

Non-validation scope:
- exact non-price evidence URL verification;
- full production scoring impact;
- final patch promotion.

## 24. Shadow Weight Calibration

```jsonl
{"row_type": "shadow_weight", "axis": "stage2_required_bridge", "scope": "canonical_archetype", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "baseline_value": "generic_stage2_bonus_allowed", "tested_value": "require_backlog_plus_margin_bridge", "delta": "guard_only", "reason": "counterexample shows equipment beta without fresh backlog/margin bridge produced weak MFE/high MAE", "backtest_effect": "3 positives preserved, 1 false positive demoted", "trigger_ids": "C01_R1L100_329180_shipbuilding_backlog_margin_bridge_T1|C01_R1L100_010620_midsize_ship_backlog_margin_bridge_T1|C01_R1L100_071970_ship_engine_backlog_high_mae_success_T1|C01_R1L100_042670_machinery_beta_no_backlog_margin_bridge_T1", "calibration_usable_count": 4, "new_independent_case_count": 4, "counterexample_count": 1, "confidence": "low_to_medium_source_proxy_only", "proposal_type": "canonical_shadow_only", "notes": "Do not promote until exact evidence URLs are added."}
{"row_type": "shadow_weight", "axis": "high_mae_success_entry_guard", "scope": "canonical_archetype", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "baseline_value": "stage2_entry_allowed", "tested_value": "entry_guard_if_MAE90_lt_minus_10_without_stage3_confirmation", "delta": "watch_guard", "reason": "ship-engine success shows high MFE but deeper MAE before confirmation", "backtest_effect": "keeps positive but avoids overconfident Green", "trigger_ids": "C01_R1L100_071970_ship_engine_backlog_high_mae_success_T1", "calibration_usable_count": 1, "new_independent_case_count": 1, "counterexample_count": 0, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "Stress-test only."}
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "C01_R1L100_329180_shipbuilding_backlog_margin_bridge", "symbol": "329180", "company_name": "HD현대중공업", "round": "R1", "loop": "100", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "LARGE_SHIPBUILDING_BACKLOG_AND_MARGIN_CONVERSION", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_structural_backlog_margin_bridge_price_confirmed", "current_profile_verdict": "current_profile_correct", "price_source": "Songdaiki/stock-web", "notes": "Large shipbuilding backlog plus margin-conversion narrative behaved like C01 rather than a simple shipbuilding beta chase. Price path supported early Stage2 but full Green still requires confirmed margin/revision."}
{"row_type": "case", "case_id": "C01_R1L100_010620_midsize_ship_backlog_margin_bridge", "symbol": "010620", "company_name": "HD현대미포", "round": "R1", "loop": "100", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "MID_SIZE_SHIP_ORDER_BACKLOG_MARGIN_TURNAROUND", "case_type": "structural_success", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_turnaround_backlog_margin_bridge_price_confirmed", "current_profile_verdict": "current_profile_correct_but_green_late_risk", "price_source": "Songdaiki/stock-web", "notes": "Backlog-to-margin bridge worked with a clean price path. The run-up also shows why Green should not be loosened: much of the upside appeared before full public confirmation."}
{"row_type": "case", "case_id": "C01_R1L100_071970_ship_engine_backlog_high_mae_success", "symbol": "071970", "company_name": "HD현대마린엔진", "round": "R1", "loop": "100", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIP_ENGINE_ORDER_BACKLOG_HIGH_MAE_SUCCESS", "case_type": "high_mae_success", "positive_or_counterexample": "positive", "best_trigger": "Stage2-Actionable", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_but_high_mae_before_backlog_bridge_confirms", "current_profile_verdict": "current_profile_correct_with_high_mae_guardrail_needed", "price_source": "Songdaiki/stock-web", "notes": "Engine backlog route worked, but the MAE is deeper than the large shipyard case. This supports C01 Stage2 only when backlog and margin bridge are both present, not generic ship/engine beta."}
{"row_type": "case", "case_id": "C01_R1L100_042670_machinery_beta_no_backlog_margin_bridge", "symbol": "042670", "company_name": "HD현대인프라코어", "round": "R1", "loop": "100", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "CONSTRUCTION_MACHINERY_EQUIPMENT_BETA_NO_BACKLOG_MARGIN_BRIDGE", "case_type": "failed_rerating", "positive_or_counterexample": "counterexample", "best_trigger": "Stage2-FalsePositive-EquipmentBetaNoFreshBacklogMarginBridge", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "counterexample_equipment_beta_without_order_backlog_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_stage2_bonus_uses_equipment_beta_only", "price_source": "Songdaiki/stock-web", "notes": "Machinery/equipment beta without a fresh backlog and margin bridge produced weak MFE and double-digit MAE. This is the control case that prevents C01 from becoming a generic industrial beta bucket."}
{"row_type": "trigger", "trigger_id": "C01_R1L100_329180_shipbuilding_backlog_margin_bridge_T1", "case_id": "C01_R1L100_329180_shipbuilding_backlog_margin_bridge", "symbol": "329180", "company_name": "HD현대중공업", "round": "R1", "loop": "100", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "LARGE_SHIPBUILDING_BACKLOG_AND_MARGIN_CONVERSION", "sector": "industrials / order backlog / shipbuilding machinery margin bridge", "primary_archetype": "order_backlog_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-18", "entry_date": "2024-04-18", "entry_price": 120300, "evidence_available_at_that_date": "source_proxy_only: historical public order/backlog/margin-turnaround narrative; exact URL pending", "evidence_source": "source_proxy_only; evidence_url_pending=true", "stage2_evidence_fields": ["public_order_backlog_visibility", "relative_strength", "backlog_or_delivery_visibility", "early_revision_signal"], "stage3_evidence_fields": ["confirmed_revision_proxy", "margin_bridge_proxy", "financial_visibility_proxy", "low_red_team_risk"], "stage4b_evidence_fields": ["valuation_rerating_watch_after_80pct_mfe", "positioning_overheat_watch"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/329/329180/2024.csv", "profile_path": "atlas/symbol_profiles/329/329180.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 21.36, "MFE_90D_pct": 84.95, "MFE_180D_pct": 84.95, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -6.48, "MAE_90D_pct": -6.48, "MAE_180D_pct": -6.48, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-09", "peak_price": 222500, "drawdown_after_peak_pct": -22.56, "green_lateness_ratio": "not_applicable_no_confirmed_green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "watch_only_after_successful_mfe", "four_b_evidence_type": ["valuation_blowoff_watch", "positioning_overheat_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "positive_structural_backlog_margin_bridge_price_confirmed", "current_profile_verdict": "current_profile_correct", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_for_2024_window", "same_entry_group_id": "C01_R1L100_329180_shipbuilding_backlog_margin_bridge_entry", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C01_R1L100_010620_midsize_ship_backlog_margin_bridge_T1", "case_id": "C01_R1L100_010620_midsize_ship_backlog_margin_bridge", "symbol": "010620", "company_name": "HD현대미포", "round": "R1", "loop": "100", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "MID_SIZE_SHIP_ORDER_BACKLOG_MARGIN_TURNAROUND", "sector": "industrials / order backlog / shipbuilding machinery margin bridge", "primary_archetype": "order_backlog_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-18", "entry_date": "2024-04-18", "entry_price": 64900, "evidence_available_at_that_date": "source_proxy_only: historical public order/backlog/margin-turnaround narrative; exact URL pending", "evidence_source": "source_proxy_only; evidence_url_pending=true", "stage2_evidence_fields": ["public_order_backlog_visibility", "relative_strength", "backlog_or_delivery_visibility"], "stage3_evidence_fields": ["margin_bridge_proxy", "financial_visibility_proxy", "repeat_order_or_conversion_proxy"], "stage4b_evidence_fields": ["valuation_blowoff_watch"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010620/2024.csv", "profile_path": "atlas/symbol_profiles/010/010620.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 22.34, "MFE_90D_pct": 61.17, "MFE_180D_pct": 61.17, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -8.17, "MAE_90D_pct": -8.17, "MAE_180D_pct": -8.17, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-17", "peak_price": 104600, "drawdown_after_peak_pct": -12.72, "green_lateness_ratio": "not_applicable_no_confirmed_green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "watch_only_after_successful_mfe", "four_b_evidence_type": ["valuation_blowoff_watch", "positioning_overheat_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "positive_turnaround_backlog_margin_bridge_price_confirmed", "current_profile_verdict": "current_profile_correct_but_green_late_risk", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_for_2024_window", "same_entry_group_id": "C01_R1L100_010620_midsize_ship_backlog_margin_bridge_entry", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C01_R1L100_071970_ship_engine_backlog_high_mae_success_T1", "case_id": "C01_R1L100_071970_ship_engine_backlog_high_mae_success", "symbol": "071970", "company_name": "HD현대마린엔진", "round": "R1", "loop": "100", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "SHIP_ENGINE_ORDER_BACKLOG_HIGH_MAE_SUCCESS", "sector": "industrials / order backlog / shipbuilding machinery margin bridge", "primary_archetype": "order_backlog_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-04-18", "entry_date": "2024-04-18", "entry_price": 13990, "evidence_available_at_that_date": "source_proxy_only: historical public order/backlog/margin-turnaround narrative; exact URL pending", "evidence_source": "source_proxy_only; evidence_url_pending=true", "stage2_evidence_fields": ["public_order_backlog_visibility", "relative_strength", "backlog_or_delivery_visibility"], "stage3_evidence_fields": ["margin_bridge_proxy", "durable_customer_confirmation_proxy"], "stage4b_evidence_fields": ["positioning_overheat_watch", "valuation_blowoff_watch"], "stage4c_evidence_fields": [], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/071/071970/2024.csv", "profile_path": "atlas/symbol_profiles/071/071970.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 27.23, "MFE_90D_pct": 63.69, "MFE_180D_pct": 63.69, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -8.15, "MAE_90D_pct": -13.15, "MAE_180D_pct": -13.15, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-17", "peak_price": 22900, "drawdown_after_peak_pct": -15.07, "green_lateness_ratio": "not_applicable_no_confirmed_green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "watch_only_after_successful_mfe", "four_b_evidence_type": ["valuation_blowoff_watch", "positioning_overheat_watch"], "four_c_protection_label": "not_applicable", "trigger_outcome_label": "positive_but_high_mae_before_backlog_bridge_confirms", "current_profile_verdict": "current_profile_correct_with_high_mae_guardrail_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_for_2024_window", "same_entry_group_id": "C01_R1L100_071970_ship_engine_backlog_high_mae_success_entry", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "trigger", "trigger_id": "C01_R1L100_042670_machinery_beta_no_backlog_margin_bridge_T1", "case_id": "C01_R1L100_042670_machinery_beta_no_backlog_margin_bridge", "symbol": "042670", "company_name": "HD현대인프라코어", "round": "R1", "loop": "100", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "CONSTRUCTION_MACHINERY_EQUIPMENT_BETA_NO_BACKLOG_MARGIN_BRIDGE", "sector": "industrials / order backlog / shipbuilding machinery margin bridge", "primary_archetype": "order_backlog_margin_bridge", "loop_objective": "coverage_gap_fill | counterexample_mining | stage2_actionable_bonus_stress_test | 4B_non_price_requirement_stress_test | canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive-EquipmentBetaNoFreshBacklogMarginBridge", "trigger_date": "2024-02-02", "entry_date": "2024-02-02", "entry_price": 8400, "evidence_available_at_that_date": "source_proxy_only: historical public order/backlog/margin-turnaround narrative; exact URL pending", "evidence_source": "source_proxy_only; evidence_url_pending=true", "stage2_evidence_fields": ["relative_strength"], "stage3_evidence_fields": [], "stage4b_evidence_fields": ["price_only_local_peak", "margin_or_backlog_slowdown"], "stage4c_evidence_fields": ["thesis_evidence_broken"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/042/042670/2024.csv", "profile_path": "atlas/symbol_profiles/042/042670.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "MFE_30D_pct": 0.71, "MFE_90D_pct": 3.69, "MFE_180D_pct": 3.69, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -13.21, "MAE_90D_pct": -13.21, "MAE_180D_pct": -13.21, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-28", "peak_price": 8710, "drawdown_after_peak_pct": -18.48, "green_lateness_ratio": "not_applicable_no_confirmed_green_trigger", "four_b_local_peak_proximity": null, "four_b_full_window_peak_proximity": null, "four_b_timing_verdict": "not_full_4B_without_non_price_evidence", "four_b_evidence_type": ["price_only"], "four_c_protection_label": "thesis_break_watch_only", "trigger_outcome_label": "counterexample_equipment_beta_without_order_backlog_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_stage2_bonus_uses_equipment_beta_only", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_by_profile_for_2024_window", "same_entry_group_id": "C01_R1L100_042670_machinery_beta_no_backlog_margin_bridge_entry", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C01_R1L100_329180_shipbuilding_backlog_margin_bridge", "trigger_id": "C01_R1L100_329180_shipbuilding_backlog_margin_bridge_T1", "symbol": "329180", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "raw_component_scores_before": {"contract_score": 55, "backlog_visibility_score": 60, "margin_bridge_score": 45, "revision_score": 45, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 10, "valuation_repricing_score": 40, "execution_risk_score": 25, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 67, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 70, "backlog_visibility_score": 75, "margin_bridge_score": 65, "revision_score": 55, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 10, "valuation_repricing_score": 40, "execution_risk_score": 20, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage3-Yellow", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C01 should require backlog visibility plus margin bridge. Generic equipment/industrial beta is demoted even if relative strength appears.", "MFE_90D_pct": 84.95, "MAE_90D_pct": -6.48, "score_return_alignment_label": "positive_structural_backlog_margin_bridge_price_confirmed", "current_profile_verdict": "current_profile_correct"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C01_R1L100_010620_midsize_ship_backlog_margin_bridge", "trigger_id": "C01_R1L100_010620_midsize_ship_backlog_margin_bridge_T1", "symbol": "010620", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "raw_component_scores_before": {"contract_score": 55, "backlog_visibility_score": 60, "margin_bridge_score": 45, "revision_score": 45, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 10, "valuation_repricing_score": 40, "execution_risk_score": 25, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 67, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 70, "backlog_visibility_score": 75, "margin_bridge_score": 65, "revision_score": 55, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 10, "valuation_repricing_score": 40, "execution_risk_score": 20, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage3-Yellow", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C01 should require backlog visibility plus margin bridge. Generic equipment/industrial beta is demoted even if relative strength appears.", "MFE_90D_pct": 61.17, "MAE_90D_pct": -8.17, "score_return_alignment_label": "positive_turnaround_backlog_margin_bridge_price_confirmed", "current_profile_verdict": "current_profile_correct_but_green_late_risk"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C01_R1L100_071970_ship_engine_backlog_high_mae_success", "trigger_id": "C01_R1L100_071970_ship_engine_backlog_high_mae_success_T1", "symbol": "071970", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "raw_component_scores_before": {"contract_score": 55, "backlog_visibility_score": 60, "margin_bridge_score": 45, "revision_score": 45, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 10, "valuation_repricing_score": 40, "execution_risk_score": 25, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 67, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 70, "backlog_visibility_score": 75, "margin_bridge_score": 65, "revision_score": 55, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 10, "valuation_repricing_score": 40, "execution_risk_score": 20, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 78, "stage_label_after": "Stage3-Yellow", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C01 should require backlog visibility plus margin bridge. Generic equipment/industrial beta is demoted even if relative strength appears.", "MFE_90D_pct": 63.69, "MAE_90D_pct": -13.15, "score_return_alignment_label": "positive_but_high_mae_before_backlog_bridge_confirms", "current_profile_verdict": "current_profile_correct_with_high_mae_guardrail_needed"}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "C01_R1L100_042670_machinery_beta_no_backlog_margin_bridge", "trigger_id": "C01_R1L100_042670_machinery_beta_no_backlog_margin_bridge_T1", "symbol": "042670", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "raw_component_scores_before": {"contract_score": 20, "backlog_visibility_score": 15, "margin_bridge_score": 5, "revision_score": 10, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 10, "valuation_repricing_score": 40, "execution_risk_score": 60, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_before": 62, "stage_label_before": "Stage2", "raw_component_scores_after": {"contract_score": 15, "backlog_visibility_score": 10, "margin_bridge_score": 0, "revision_score": 10, "relative_strength_score": 70, "customer_quality_score": 35, "policy_or_regulatory_score": 10, "valuation_repricing_score": 40, "execution_risk_score": 70, "legal_or_contract_risk_score": 15, "dilution_cb_risk_score": 0, "accounting_trust_risk_score": 0}, "weighted_score_after": 55, "stage_label_after": "Stage1/weak-watch", "changed_components": ["backlog_visibility_score", "margin_bridge_score", "execution_risk_score"], "component_delta_explanation": "C01 should require backlog visibility plus margin bridge. Generic equipment/industrial beta is demoted even if relative strength appears.", "MFE_90D_pct": 3.69, "MAE_90D_pct": -13.21, "score_return_alignment_label": "counterexample_equipment_beta_without_order_backlog_margin_bridge", "current_profile_verdict": "current_profile_false_positive_if_stage2_bonus_uses_equipment_beta_only"}
{"row_type": "shadow_weight", "axis": "stage2_required_bridge", "scope": "canonical_archetype", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "baseline_value": "generic_stage2_bonus_allowed", "tested_value": "require_backlog_plus_margin_bridge", "delta": "guard_only", "reason": "counterexample shows equipment beta without fresh backlog/margin bridge produced weak MFE/high MAE", "backtest_effect": "3 positives preserved, 1 false positive demoted", "trigger_ids": "C01_R1L100_329180_shipbuilding_backlog_margin_bridge_T1|C01_R1L100_010620_midsize_ship_backlog_margin_bridge_T1|C01_R1L100_071970_ship_engine_backlog_high_mae_success_T1|C01_R1L100_042670_machinery_beta_no_backlog_margin_bridge_T1", "calibration_usable_count": 4, "new_independent_case_count": 4, "counterexample_count": 1, "confidence": "low_to_medium_source_proxy_only", "proposal_type": "canonical_shadow_only", "notes": "Do not promote until exact evidence URLs are added."}
{"row_type": "shadow_weight", "axis": "high_mae_success_entry_guard", "scope": "canonical_archetype", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "baseline_value": "stage2_entry_allowed", "tested_value": "entry_guard_if_MAE90_lt_minus_10_without_stage3_confirmation", "delta": "watch_guard", "reason": "ship-engine success shows high MFE but deeper MAE before confirmation", "backtest_effect": "keeps positive but avoids overconfident Green", "trigger_ids": "C01_R1L100_071970_ship_engine_backlog_high_mae_success_T1", "calibration_usable_count": 1, "new_independent_case_count": 1, "counterexample_count": 0, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "Stress-test only."}
{"row_type": "residual_contribution", "round": "R1", "loop": "100", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "same_archetype_new_symbol_count": 4, "same_archetype_new_trigger_family_count": 2, "new_trigger_family_count": 2, "positive_case_count": 3, "counterexample_count": 1, "current_profile_error_count": 1, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["equipment_beta_without_backlog_margin_bridge_false_positive", "high_mae_success_requires_entry_guard"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
```

## 26. Deferred Coding Agent Handoff Prompt

### Purpose

You are now in the repository implementation phase. The attached Markdown file is a v12 post-calibrated residual research output produced using the Songdaiki/stock-web OHLC atlas.

This MD is not live candidate research. It is historical calibration research designed to extend the already-applied e2r_2_2 rolling calibrated profile.

### Price source context

- Primary historical price source used by the research MD: Songdaiki/stock-web.
- Price basis: tradable_raw.
- Price adjustment status: raw_unadjusted_marcap.
- Price shard pattern: atlas/ohlcv_tradable_by_symbol_year/<prefix>/<ticker>/<year>.csv.
- Symbol profile pattern: atlas/symbol_profiles/<prefix>/<ticker>.json.

### Rules

- Use only calibration_usable=true rows for quantitative calibration.
- Do not count reused cases as new independent evidence unless independent_evidence_weight > 0.
- Do not treat source_proxy_only rows as promotion-ready.
- Do not apply global deltas.
- Keep C01 guard as shadow-only until exact evidence URLs are added.
- Positive score promotion requires backlog visibility plus margin bridge.

## 27. Next Round State

```text
completed_round = R1
completed_loop = 100
selection_basis = docs/core/V12_Research_No_Repeat_Index.md
selected_priority_bucket = Priority 0
next_recommended_archetypes = C07_HBM_EQUIPMENT_ORDER_RELATIVE_STRENGTH, C06_HBM_MEMORY_CUSTOMER_CAPACITY, C10_MEMORY_RECOVERY_EQUIPMENT_CYCLE, C14_EV_DEMAND_SLOWDOWN_4B_4C
round_schedule_status = coverage_index_selected
round_sector_consistency = pass
```

## 28. Source Notes

- `docs/core/e2r_v12_prompt_round_scheduler_corrected.txt` was treated as the execution prompt.
- `docs/core/V12_Research_No_Repeat_Index.md` was used only as the no-repeat and coverage ledger.
- Stock-Web manifest/schema/profile/shard data were used for price path validation.
- Evidence URL status: `evidence_url_pending=true`.
- Promotion status: `shadow_only`.
