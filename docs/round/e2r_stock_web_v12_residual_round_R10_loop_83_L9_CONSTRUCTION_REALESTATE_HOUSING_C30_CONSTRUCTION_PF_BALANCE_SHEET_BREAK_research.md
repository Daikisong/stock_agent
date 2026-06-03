# E2R Stock-Web v12 Residual Research — R10 Loop 83 / L9 / C30

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R10",
  "scheduled_loop": 83,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R10",
  "completed_loop": 83,
  "computed_next_round": "R11",
  "computed_next_loop": 83,
  "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING",
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "fine_archetype_id": "PF_REFINANCING_ORDERBOOK_BALANCE_SHEET_RECOVERY_VS_HOUSING_THEME_FALSE_POSITIVE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "PF_refinancing_balance_sheet_guardrail",
    "4B_non_price_requirement_stress_test",
    "hard_4C_thesis_break_protection",
    "canonical_archetype_compression",
    "source_repair_queue_creation"
  ],
  "price_source": "Songdaiki/stock-web",
  "price_basis": "tradable_raw",
  "price_adjustment_status": "raw_unadjusted_marcap",
  "stock_web_manifest_max_date": "2026-02-20",
  "production_scoring_changed": false,
  "shadow_weight_only": true,
  "handoff_prompt_executed_now": false,
  "do_not_propose_new_weight_delta": true
}
```

## 1. Current Calibrated Profile Assumption

```text
current_default_profile_proxy = e2r_2_1_stock_web_calibrated
previous_baseline_reference = e2r_2_0_baseline
production_scoring_changed = false
shadow_weight_only = true
handoff_prompt_executed_now = false
```

This file is a standalone historical calibration / sector-archetype residual research artifact. It does not patch `stock_agent`, does not run live discovery, and does not propose immediate production scoring changes.

## 2. Round / Large Sector / Canonical Archetype Scope

```text
scheduled_round = R10
scheduled_loop = 83
allowed_large_sector = L9_CONSTRUCTION_REALESTATE_HOUSING
selected_large_sector = L9_CONSTRUCTION_REALESTATE_HOUSING
selected_canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
computed_next_round = R11
computed_next_loop = 83
round_schedule_status = valid
round_sector_consistency = pass
```

R10 is the construction / real estate / housing round. This run uses C30 because the residual being tested is the boundary between:

```text
housing / construction recovery headline
```

and

```text
PF refinancing + debt/liquidity control + project-loss visibility + orderbook quality + margin bridge
```

The mechanism is like checking whether a cracked bridge has been repaired before letting traffic back on it. A housing rebound headline is traffic. PF refinancing, cash flow, loss provisioning and backlog margin are the bridge.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C30 is already covered by names such as `047040`, `006360`, `UNKNOWN_SYMBOL`, `294870`, `005960`, and `000720`. This run avoids those top-covered symbols and uses:

```text
375500 / DL이앤씨
010780 / 아이에스동서
002990 / 금호건설
```

All three are treated as new independent C30 cases for this loop. No hard duplicate is intentionally reused.

## 4. Stock-Web OHLC Input / Price Source Validation

```text
price_source = Songdaiki/stock-web
source_basis = FinanceData/marcap transformed into symbol-year CSV shards
price_basis = tradable_raw
price_adjustment_status = raw_unadjusted_marcap
manifest_max_date = 2026-02-20
calibration_shard_root = atlas/ohlcv_tradable_by_symbol_year
```

Per-symbol profile status:

| symbol | company | profile path | corporate-action caveat |
|---|---|---|---|
| 375500 | DL이앤씨 | `atlas/symbol_profiles/375/375500.json` | old 2022 CA candidates; selected 2024/2025 forward window clean |
| 010780 | 아이에스동서 | `atlas/symbol_profiles/010/010780.json` | old CA candidates through 2011; selected 2024 forward window clean |
| 002990 | 금호건설 | `atlas/symbol_profiles/002/002990.json` | old CA candidates through 2013; selected 2024/2025 forward window clean |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R10L83-C30-01 | 375500 | 2024-07-12 | 33,400 | 180D | clean | true |
| R10L83-C30-02 | 010780 | 2024-03-08 | 30,100 | 180D | clean | true |
| R10L83-C30-03 | 002990 | 2024-01-30 | 5,200 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | LARGE_BUILDER_ORDERBOOK_BALANCE_SHEET_RECOVERY | keep Stage2 only when PF exposure is ring-fenced and orderbook/margin bridge is visible |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | HOUSING_THEME_FALSE_POSITIVE | reject Stage2 when recovery is only housing/PF sentiment without refinancing and margin repair |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | SMALL_MID_BUILDER_4C_WATCH | route to RiskWatch/4C-watch when debt/liquidity, PF refinancing or project-loss thesis is unresolved |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R10L83-C30-01 | 375500 | DL이앤씨 | Stage2-Actionable | 2024-07-12 | 33,400 | 40.57 | -14.37 | current_profile_partially_correct_high_MAE_watch_needed |
| R10L83-C30-02 | 010780 | 아이에스동서 | Stage2-FalsePositive | 2024-03-08 | 30,100 | 3.65 | -32.39 | current_profile_false_positive |
| R10L83-C30-03 | 002990 | 금호건설 | Stage2-FalsePositive | 2024-01-30 | 5,200 | 1.54 | -53.37 | current_profile_false_positive_4C_late |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_or_4C_case_count = 2
calibration_usable_case_count = 3
new_independent_case_count = 3
```

## 9. Evidence Source Map

All selected evidence is currently `source_proxy_only=true / evidence_url_pending=true`.

This MD therefore creates a source-repair queue and a C30 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: PF refinancing, debt maturity, cash flow, project-loss provisioning, orderbook quality, margin bridge, company disclosure, report or filing evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 375500 | `atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv` and `2025.csv` | `atlas/symbol_profiles/375/375500.json` |
| 010780 | `atlas/ohlcv_tradable_by_symbol_year/010/010780/2024.csv` | `atlas/symbol_profiles/010/010780.json` |
| 002990 | `atlas/ohlcv_tradable_by_symbol_year/002/002990/2024.csv` and `2025.csv` | `atlas/symbol_profiles/002/002990.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 375500 / DL이앤씨

C30 recovery positive with high-MAE watch. The price path eventually recovered meaningfully, but only after a deep enough drawdown to remind the model that construction Stage2 should be balanced-sheet aware. The correct interpretation is not “construction bottomed.” It is “the case can stay Stage2 if PF exposure, orderbook quality and margin normalization survive source repair.”

### Case 2 — 010780 / 아이에스동서

C30 housing recovery false positive. A housing or construction recovery narrative produced a small MFE and then a large MAE. This is the bucket where Stage2-Actionable should be blocked unless refinancing, project-loss path and cash-flow bridge are explicit.

### Case 3 — 002990 / 금호건설

C30 small/mid builder false positive with 4C-watch flavor. The initial MFE was tiny and the later MAE was deep. Small/mid construction names need a stricter debt/PF bridge gate because solvency and project-loss risk can dominate any housing-recovery narrative.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 375500 | 33,400 | 7.78 | -14.37 | 7.78 | -14.37 | 40.57 | -14.37 | 2025-03-10 / 46,950 | -20.87 |
| 010780 | 30,100 | 3.65 | -18.44 | 3.65 | -18.44 | 3.65 | -32.39 | 2024-03-22 / 31,200 | -34.78 |
| 002990 | 5,200 | 1.54 | -7.40 | 1.54 | -23.75 | 1.54 | -53.37 | 2024-02-01 / 5,280 | -54.07 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R10L83-C30-01 | Stage2-Actionable if bridge exists | large later MFE, but high initial MAE | partially correct; high-MAE watch required |
| R10L83-C30-02 | risk of treating housing recovery as Stage2 | tiny MFE / large MAE | false positive |
| R10L83-C30-03 | risk of treating low-PBR construction as Stage2 | tiny MFE / deep MAE | false positive / 4C-watch late |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C30, the residual is not Green lateness. The residual is whether Stage2-Actionable is allowed before PF refinancing, debt/liquidity, project-loss and margin bridge are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R10L83-C30-01 | 0.75 | 0.70 | local 4B watch after balance-sheet recovery matures |
| R10L83-C30-02 | 0.15 | 0.15 | housing theme rejected without PF/margin bridge |
| R10L83-C30-03 | 0.15 | 0.15 | route to RiskWatch or 4C-watch when debt/PF bridge absent |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_thesis_break
hard_4c_price_only_allowed = false
```

The `002990` path is a 4C-watch / hard-thesis-break candidate only after non-price evidence confirms debt/liquidity or project-loss break. Price decline alone is not used as hard 4C evidence.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = construction/PF rows need PF refinancing, debt/liquidity, project-loss and margin bridge before Stage2-Actionable
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
candidate_axis = C30_PF_refinancing_debt_margin_bridge_required
effect = keep bridge-positive recovery cases, demote housing-theme-only false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 4.32 | -18.85 | may over-credit housing/PF sentiment | needs C30 bridge repair |
| P1 canonical shadow bridge profile | 3 | 7.78 on kept positive | -14.37 on kept positive | demotes 010780/002990 | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R10L83-C30-01 | 78 | Stage2-Actionable | 80 | Stage2-Actionable + high-MAE/PF RiskWatch | partially aligned |
| R10L83-C30-02 | 58 | Stage2-Watch/FalsePositive | 49 | Rejected-Stage2 / RiskWatch | improved |
| R10L83-C30-03 | 58 | Stage2-Watch/FalsePositive | 49 | Rejected-Stage2 / RiskWatch or 4C-watch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | PF_REFINANCING_ORDERBOOK_BALANCE_SHEET_RECOVERY_VS_HOUSING_THEME_FALSE_POSITIVE | 1 | 2 | 1 | 1-watch | 3 | 0 | 3 | 2 | no | yes | source repair needed |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 3
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 3
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 3
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
residual_error_types_found:
  - housing_theme_false_positive_high_MAE
  - PF_refinancing_bridge_required
  - debt_liquidity_project_loss_margin_bridge_required
  - 4C_watch_late_for_small_mid_builder
new_axis_proposed: false
existing_axis_strengthened: C30_PF_refinancing_debt_margin_bridge_required
existing_axis_weakened: null
existing_axis_kept: full_4b_requires_non_price_evidence, hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C30_PF_refinancing_debt_margin_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent cases, 2 counterexamples, and 2 residual errors for R10/L9_CONSTRUCTION_REALESTATE_HOUSING/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK.

## 23. Validation Scope / Non-Validation Scope

Validated in this MD:

```text
- Stock-Web profile path exists for selected symbols
- Stock-Web tradable shard path exists for selected symbols
- entry_date / entry_price are taken from tradable_raw close
- MFE / MAE / peak / post-peak drawdown are computed from observed OHLC windows
- corporate-action windows are checked at profile level
```

Not validated in this MD:

```text
- primary evidence URL
- exact publication time
- PF refinancing detail
- debt maturity and liquidity bridge
- project-loss provisioning detail
- cash-flow and margin normalization
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C30_PF_refinancing_debt_margin_bridge_required,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"Require PF refinancing, debt/liquidity, project-loss and margin bridge before Stage2-Actionable","keeps 375500 with high-MAE watch; demotes 010780/002990","R10L83-C30-01-S2A-20240712|R10L83-C30-02-S2FP-20240308|R10L83-C30-03-S2FP-20240130",3,3,2,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R10L83-C30-01", "symbol": "375500", "company_name": "DL이앤씨", "round": "R10", "loop": 83, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_REFINANCING_ORDERBOOK_BALANCE_SHEET_RECOVERY_VS_HOUSING_THEME_FALSE_POSITIVE", "case_type": "balance_sheet_orderbook_recovery_positive", "positive_or_counterexample": "positive", "best_trigger": "R10L83-C30-01-S2A-20240712", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_recovery_with_high_MAE_and_later_4B_watch", "current_profile_verdict": "current_profile_partially_correct_high_MAE_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C30 recovery can remain Stage2 only if PF exposure is ring-fenced and orderbook/margin bridge is visible."}
{"row_type": "trigger", "trigger_id": "R10L83-C30-01-S2A-20240712", "case_id": "R10L83-C30-01", "symbol": "375500", "company_name": "DL이앤씨", "round": "R10", "loop": 83, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_REFINANCING_ORDERBOOK_BALANCE_SHEET_RECOVERY_VS_HOUSING_THEME_FALSE_POSITIVE", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|hard_4C_thesis_break_protection|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-12", "evidence_available_at_that_date": "large-construction balance-sheet/orderbook recovery proxy; PF exposure and margin bridge pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["PF_refinancing_or_debt_bridge", "orderbook_quality", "project_margin_bridge_proxy"], "stage3_evidence_fields": ["loss_provision_path", "cash_flow_bridge", "balance_sheet_trust", "margin_normalization"], "stage4b_evidence_fields": ["valuation_recovery_overheat", "PF_refinancing_gap", "post_peak_drawdown"], "stage4c_evidence_fields": ["debt_liquidity_break_watch", "hard_project_loss_or_default_watch"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv", "profile_path": "atlas/symbol_profiles/375/375500.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-12", "entry_price": 33400, "MFE_30D_pct": 7.78, "MFE_90D_pct": 7.78, "MFE_180D_pct": 40.57, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -14.37, "MAE_90D_pct": -14.37, "MAE_180D_pct": -14.37, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-03-10", "peak_price": 46950, "drawdown_after_peak_pct": -20.87, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.75, "four_b_full_window_peak_proximity": 0.7, "four_b_timing_verdict": "local_4B_watch_after_balance_sheet_recovery_matures", "four_b_evidence_type": ["PF_refinancing_gap", "valuation_recovery_overheat", "post_peak_drawdown"], "four_c_protection_label": "hard_4C_requires_non_price_thesis_break", "trigger_outcome_label": "positive_recovery_with_high_MAE_and_later_4B_watch", "current_profile_verdict": "current_profile_partially_correct_high_MAE_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2022_CA_candidates", "same_entry_group_id": "R10L83-C30-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L83-C30-01", "trigger_id": "R10L83-C30-01-S2A-20240712", "symbol": "375500", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 40, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 45, "customer_quality_score": 35, "policy_or_regulatory_score": 10, "valuation_repricing_score": 55, "execution_risk_score": 45, "PF_refinancing_risk_score": 35, "debt_liquidity_risk_score": 30, "project_loss_risk_score": 35, "balance_sheet_trust_score": 45, "orderbook_quality_score": 45}, "weighted_score_before": 78, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 40, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 45, "customer_quality_score": 35, "policy_or_regulatory_score": 10, "valuation_repricing_score": 55, "execution_risk_score": 45, "PF_refinancing_risk_score": 40, "debt_liquidity_risk_score": 30, "project_loss_risk_score": 35, "balance_sheet_trust_score": 50, "orderbook_quality_score": 45}, "weighted_score_after": 80, "stage_label_after": "Stage2-Actionable + high-MAE/PF RiskWatch", "changed_components": ["PF_refinancing_risk_score", "debt_liquidity_risk_score", "margin_bridge_score", "balance_sheet_trust_score"], "component_delta_explanation": "C30 requires PF refinancing, debt/liquidity, project-loss and margin bridge before Stage2-Actionable; housing-theme-only cases are demoted.", "MFE_90D_pct": 7.78, "MAE_90D_pct": -14.37, "score_return_alignment_label": "positive_recovery_with_high_MAE_and_later_4B_watch", "current_profile_verdict": "current_profile_partially_correct_high_MAE_watch_needed"}
{"row_type": "case", "case_id": "R10L83-C30-02", "symbol": "010780", "company_name": "아이에스동서", "round": "R10", "loop": 83, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_REFINANCING_ORDERBOOK_BALANCE_SHEET_RECOVERY_VS_HOUSING_THEME_FALSE_POSITIVE", "case_type": "housing_recovery_theme_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R10L83-C30-02-S2FP-20240308", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "false_positive_low_MFE_high_MAE", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Housing recovery is not enough; the model needs PF refinancing visibility, loss-provision path, and margin normalization."}
{"row_type": "trigger", "trigger_id": "R10L83-C30-02-S2FP-20240308", "case_id": "R10L83-C30-02", "symbol": "010780", "company_name": "아이에스동서", "round": "R10", "loop": 83, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_REFINANCING_ORDERBOOK_BALANCE_SHEET_RECOVERY_VS_HOUSING_THEME_FALSE_POSITIVE", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|hard_4C_thesis_break_protection|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-03-08", "evidence_available_at_that_date": "housing/PF recovery theme proxy without refinancing, project-loss and margin bridge confirmation", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["PF_refinancing_or_debt_bridge", "orderbook_quality", "project_margin_bridge_proxy"], "stage3_evidence_fields": ["loss_provision_path", "cash_flow_bridge", "balance_sheet_trust", "margin_normalization"], "stage4b_evidence_fields": ["valuation_recovery_overheat", "PF_refinancing_gap", "post_peak_drawdown"], "stage4c_evidence_fields": ["debt_liquidity_break_watch", "hard_project_loss_or_default_watch"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010780/2024.csv", "profile_path": "atlas/symbol_profiles/010/010780.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-03-08", "entry_price": 30100, "MFE_30D_pct": 3.65, "MFE_90D_pct": 3.65, "MFE_180D_pct": 3.65, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -18.44, "MAE_90D_pct": -18.44, "MAE_180D_pct": -32.39, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-22", "peak_price": 31200, "drawdown_after_peak_pct": -34.78, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.15, "four_b_full_window_peak_proximity": 0.15, "four_b_timing_verdict": "housing_theme_rejected_without_PF_refinancing_margin_bridge", "four_b_evidence_type": ["PF_refinancing_gap", "valuation_recovery_overheat", "post_peak_drawdown"], "four_c_protection_label": "hard_4C_requires_non_price_thesis_break", "trigger_outcome_label": "false_positive_low_MFE_high_MAE", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2011_CA_candidates", "same_entry_group_id": "R10L83-C30-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L83-C30-02", "trigger_id": "R10L83-C30-02-S2FP-20240308", "symbol": "010780", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 30, "customer_quality_score": 15, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 75, "PF_refinancing_risk_score": 80, "debt_liquidity_risk_score": 75, "project_loss_risk_score": 70, "balance_sheet_trust_score": 20, "orderbook_quality_score": 15}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 30, "customer_quality_score": 15, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 75, "PF_refinancing_risk_score": 90, "debt_liquidity_risk_score": 85, "project_loss_risk_score": 70, "balance_sheet_trust_score": 10, "orderbook_quality_score": 15}, "weighted_score_after": 49, "stage_label_after": "Rejected-Stage2 / RiskWatch or 4C-watch", "changed_components": ["PF_refinancing_risk_score", "debt_liquidity_risk_score", "margin_bridge_score", "balance_sheet_trust_score"], "component_delta_explanation": "C30 requires PF refinancing, debt/liquidity, project-loss and margin bridge before Stage2-Actionable; housing-theme-only cases are demoted.", "MFE_90D_pct": 3.65, "MAE_90D_pct": -18.44, "score_return_alignment_label": "false_positive_low_MFE_high_MAE", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "case", "case_id": "R10L83-C30-03", "symbol": "002990", "company_name": "금호건설", "round": "R10", "loop": 83, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_REFINANCING_ORDERBOOK_BALANCE_SHEET_RECOVERY_VS_HOUSING_THEME_FALSE_POSITIVE", "case_type": "small_mid_builder_PF_balance_sheet_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R10L83-C30-03-S2FP-20240130", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "false_positive_low_MFE_high_MAE_4C_watch", "current_profile_verdict": "current_profile_false_positive_4C_late", "price_source": "Songdaiki/stock-web", "notes": "For smaller builders, absence of debt/PF refinancing and backlog margin bridge should block Stage2-Actionable."}
{"row_type": "trigger", "trigger_id": "R10L83-C30-03-S2FP-20240130", "case_id": "R10L83-C30-03", "symbol": "002990", "company_name": "금호건설", "round": "R10", "loop": 83, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "PF_REFINANCING_ORDERBOOK_BALANCE_SHEET_RECOVERY_VS_HOUSING_THEME_FALSE_POSITIVE", "loop_objective": "coverage_gap_fill|counterexample_mining|4B_non_price_requirement_stress_test|hard_4C_thesis_break_protection|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-01-30", "evidence_available_at_that_date": "small/mid builder construction recovery proxy without debt, PF, backlog-quality or project-margin repair", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["PF_refinancing_or_debt_bridge", "orderbook_quality", "project_margin_bridge_proxy"], "stage3_evidence_fields": ["loss_provision_path", "cash_flow_bridge", "balance_sheet_trust", "margin_normalization"], "stage4b_evidence_fields": ["valuation_recovery_overheat", "PF_refinancing_gap", "post_peak_drawdown"], "stage4c_evidence_fields": ["debt_liquidity_break_watch", "hard_project_loss_or_default_watch"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002990/2024.csv", "profile_path": "atlas/symbol_profiles/002/002990.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-30", "entry_price": 5200, "MFE_30D_pct": 1.54, "MFE_90D_pct": 1.54, "MFE_180D_pct": 1.54, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -7.4, "MAE_90D_pct": -23.75, "MAE_180D_pct": -53.37, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-01", "peak_price": 5280, "drawdown_after_peak_pct": -54.07, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.15, "four_b_full_window_peak_proximity": 0.15, "four_b_timing_verdict": "should_route_to_RiskWatch_or_4C_watch_when_debt_PF_bridge_absent", "four_b_evidence_type": ["PF_refinancing_gap", "valuation_recovery_overheat", "post_peak_drawdown"], "four_c_protection_label": "hard_4C_requires_non_price_thesis_break", "trigger_outcome_label": "false_positive_low_MFE_high_MAE_4C_watch", "current_profile_verdict": "current_profile_false_positive_4C_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2013_CA_candidates", "same_entry_group_id": "R10L83-C30-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L83-C30-03", "trigger_id": "R10L83-C30-03-S2FP-20240130", "symbol": "002990", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 30, "customer_quality_score": 15, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 75, "PF_refinancing_risk_score": 80, "debt_liquidity_risk_score": 75, "project_loss_risk_score": 70, "balance_sheet_trust_score": 20, "orderbook_quality_score": 15}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"contract_score": 10, "backlog_visibility_score": 15, "margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 30, "customer_quality_score": 15, "policy_or_regulatory_score": 10, "valuation_repricing_score": 25, "execution_risk_score": 75, "PF_refinancing_risk_score": 90, "debt_liquidity_risk_score": 85, "project_loss_risk_score": 70, "balance_sheet_trust_score": 10, "orderbook_quality_score": 15}, "weighted_score_after": 49, "stage_label_after": "Rejected-Stage2 / RiskWatch or 4C-watch", "changed_components": ["PF_refinancing_risk_score", "debt_liquidity_risk_score", "margin_bridge_score", "balance_sheet_trust_score"], "component_delta_explanation": "C30 requires PF refinancing, debt/liquidity, project-loss and margin bridge before Stage2-Actionable; housing-theme-only cases are demoted.", "MFE_90D_pct": 1.54, "MAE_90D_pct": -23.75, "score_return_alignment_label": "false_positive_low_MFE_high_MAE_4C_watch", "current_profile_verdict": "current_profile_false_positive_4C_late"}
{"row_type": "shadow_weight", "axis": "C30_PF_refinancing_debt_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Construction recovery requires PF refinancing, debt/liquidity control, project-loss visibility and orderbook/margin bridge; housing-theme-only rallies produce high MAE.", "backtest_effect": "keeps 375500 as recovery with riskwatch, rejects 010780/002990 false positives", "trigger_ids": "R10L83-C30-01-S2A-20240712|R10L83-C30-02-S2FP-20240308|R10L83-C30-03-S2FP-20240130", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 2, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R10", "loop": 83, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c"], "residual_error_types_found": ["housing_theme_false_positive_high_MAE", "PF_refinancing_bridge_required", "debt_liquidity_project_loss_margin_bridge_required", "4C_watch_late_for_small_mid_builder"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- Do not treat source_proxy_only or evidence_url_pending rows as runtime promotion-ready.
- Keep production scoring unchanged unless a later batch validates primary evidence and aggregate thresholds.
- For C30, test a canonical-archetype guard requiring PF refinancing, debt/liquidity, project-loss visibility and margin bridge before Stage2-Actionable.

## 27. Next Round State

```text
completed_round = R10
completed_loop = 83
next_round = R11
next_loop = 83
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
price_source = Songdaiki/stock-web
```
