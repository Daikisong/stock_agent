# E2R Stock-Web v12 Residual Research — R10 Loop 86 / L9 / C30

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R10",
  "scheduled_loop": 86,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R10",
  "completed_loop": 86,
  "computed_next_round": "R11",
  "computed_next_loop": 86,
  "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING",
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "fine_archetype_id": "LARGE_DEVELOPER_BUILDING_MATERIALS_MID_BUILDER_PF_DEBT_ORDERBOOK_CASHFLOW_MARGIN_BRIDGE_VS_VALUEUP_HOUSING_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "construction_PF_balance_sheet_guardrail",
    "large_builder_developer_orderbook_cashflow_margin_bridge_test",
    "construction_valueup_theme_vs_PF_debt_liquidity_bridge_split",
    "local_4B_timing_after_construction_MFE",
    "hard_4C_non_price_debt_project_loss_or_margin_break_protection",
    "source_proxy_runtime_promotion_blocker",
    "high_MAE_guardrail",
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
scheduled_loop = 86
allowed_large_sector = L9_CONSTRUCTION_REALESTATE_HOUSING
selected_large_sector = L9_CONSTRUCTION_REALESTATE_HOUSING
selected_canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
computed_next_round = R11
computed_next_loop = 86
round_schedule_status = valid
round_sector_consistency = pass
```

R10 is the construction / real estate / housing round. Loop85 R10 already tested small/mid-builder PF names, so loop86 shifts to a large-builder / developer / mid-builder mix.

The tested mechanism:

```text
construction / housing / PF recovery / value-up headline
→ PF refinancing and debt-liquidity control
→ orderbook quality and cash collection
→ project-loss path
→ project-margin bridge
→ durable rerating or construction value-up fade
```

C30 is the foundation inspection. A housing headline can lift the roof, but PF, debt, cash flow and project margin decide whether the building stands.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C30 top-covered symbols include `047040`, `006360`, `UNKNOWN_SYMBOL`, `294870`, `005960`, and `000720`. This run avoids that top-covered set and also avoids loop85 R10 symbols:

```text
previous_loop85_R10_symbols = 001260 / 017000 / 002780
selected_loop86_symbols = 010780 / 375500 / 002990
```

All three are treated as new independent C30 construction/PF balance-sheet cases for this loop. No hard duplicate is intentionally reused.

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
| 010780 | 아이에스동서 | `atlas/symbol_profiles/010/010780.json` | old CA candidates through 2011; selected 2024 forward window clean |
| 375500 | DL이앤씨 | `atlas/symbol_profiles/375/375500.json` | old 2022 CA candidates; selected 2024 forward window clean |
| 002990 | 금호건설 | `atlas/symbol_profiles/002/002990.json` | old CA candidates through 2013; selected 2024 forward window clean |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R10L86-C30-01 | 010780 | 2024-01-25 | 24,850 | 180D | clean | true |
| R10L86-C30-02 | 375500 | 2024-07-12 | 33,400 | 180D | clean | true |
| R10L86-C30-03 | 002990 | 2024-02-13 | 5,180 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | DEVELOPER_BUILDING_MATERIALS_PF_RECOVERY | keep Stage2 with PF/debt/orderbook/cash-flow bridge; add local 4B after MFE |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | LARGE_BUILDER_VALUEUP_MARGIN_GAP | reject low-MFE/high-MAE value-up rebound without PF/orderbook/project-margin bridge |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | MID_BUILDER_LOW_MFE_PF_THEME_FADE | reject very-low-MFE mid-builder theme without refinancing/liquidity/margin evidence |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R10L86-C30-01 | 010780 | 아이에스동서 | Stage2-Actionable | 2024-01-25 | 24,850 | 25.55 | -18.11 | current_profile_partially_correct_high_MAE_PF_bridge_needed |
| R10L86-C30-02 | 375500 | DL이앤씨 | Stage2-FalsePositive | 2024-07-12 | 33,400 | 7.78 | -14.37 | current_profile_false_positive_low_MFE_high_MAE |
| R10L86-C30-03 | 002990 | 금호건설 | Stage2-FalsePositive | 2024-02-13 | 5,180 | 0.97 | -38.61 | current_profile_false_positive_low_MFE_high_MAE |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 2
4B_or_4C_case_count = 3
calibration_usable_case_count = 3
new_independent_case_count = 3
```

## 9. Evidence Source Map

All selected evidence is currently `source_proxy_only=true / evidence_url_pending=true`.

This MD creates a source-repair queue and a C30 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: PF refinancing, debt maturity schedule, liquidity/cash collection, orderbook quality, project-loss provisioning, project-margin bridge, company disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 010780 | `atlas/ohlcv_tradable_by_symbol_year/010/010780/2024.csv` | `atlas/symbol_profiles/010/010780.json` |
| 375500 | `atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv` | `atlas/symbol_profiles/375/375500.json` |
| 002990 | `atlas/ohlcv_tradable_by_symbol_year/002/002990/2024.csv` | `atlas/symbol_profiles/002/002990.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 010780 / 아이에스동서

C30 developer/building-materials positive with high-MAE watch. The January trigger produced meaningful MFE into March, but later drawdown widened. This is a keep-with-guardrail row, not clean Green.

### Case 2 — 375500 / DL이앤씨

C30 large-builder value-up/PF recovery false positive. The July rebound produced only limited MFE and then a high-MAE drawdown. Large-builder value-up language should be rejected unless PF, cash-flow and project-margin evidence are explicit.

### Case 3 — 002990 / 금호건설

C30 mid-builder PF/value-up false positive. The trigger produced almost no MFE and then bled into deep MAE. This is a low-MFE construction value trap.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 010780 | 24,850 | 21.93 | -1.61 | 25.55 | -1.61 | 25.55 | -18.11 | 2024-03-22 / 31,200 | -34.78 |
| 375500 | 33,400 | 7.78 | -14.37 | 7.78 | -14.37 | 7.78 | -14.37 | 2024-07-31 / 36,000 | -20.56 |
| 002990 | 5,180 | 0.97 | -15.44 | 0.97 | -26.35 | 0.97 | -38.61 | 2024-02-19 / 5,230 | -39.20 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R10L86-C30-01 | Stage2-Actionable if PF/debt/orderbook bridge exists | MFE then deeper drawdown | partially correct; local 4B/PF bridge needed |
| R10L86-C30-02 | risk of treating large-builder rebound as Stage2 | low MFE / high MAE | false positive |
| R10L86-C30-03 | risk of treating mid-builder value-up as Stage2 | very low MFE / deep MAE | false positive |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C30, the residual is whether construction/PF MFE becomes clean Stage2/Green before refinancing, debt/liquidity, orderbook, cash-flow and project-margin bridge are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R10L86-C30-01 | 0.75 | 0.65 | local 4B watch after developer MFE if PF/debt/orderbook/margin bridge stalls |
| R10L86-C30-02 | 0.35 | 0.30 | large-builder value-up theme rejected without PF/orderbook/margin bridge |
| R10L86-C30-03 | 0.35 | 0.30 | mid-builder PF theme rejected without refinancing/liquidity/orderbook bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_debt_project_loss_or_margin_break
hard_4c_price_only_allowed = false
```

Price drawdown alone is not hard 4C. C30 hard 4C requires confirmed PF refinancing failure, debt/liquidity break, cash collection failure, project-loss provisioning, impairment, or project-margin thesis break.

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L9/C30 rows need PF refinancing, debt/liquidity control, orderbook quality, cash-flow and project-margin bridge before clean Stage2/Green
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
candidate_axis = C30_PF_debt_liquidity_orderbook_cashflow_project_margin_bridge_required
effect = keep developer positive with local 4B/high-MAE watch; demote low-MFE large/mid-builder false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 11.43 | -14.11 | may over-credit construction value-up/PF rebound language | needs C30 PF/orderbook/margin bridge repair |
| P1 canonical shadow bridge profile | 3 | 25.55 on kept positive | demotes 375500/002990 | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R10L86-C30-01 | 76 | Stage2-Actionable | 72 | Stage2-Actionable + local 4B/PF-orderbook-margin watch | partially aligned |
| R10L86-C30-02 | 58 | Stage2-Watch/FalsePositive | 43 | Rejected-Stage2 / Construction-PF value-up RiskWatch | improved |
| R10L86-C30-03 | 58 | Stage2-Watch/FalsePositive | 43 | Rejected-Stage2 / Construction-PF value-up RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | LARGE_DEVELOPER_BUILDING_MATERIALS_MID_BUILDER_PF_DEBT_ORDERBOOK_CASHFLOW_MARGIN_BRIDGE_VS_VALUEUP_HOUSING_THEME_FADE | 1 | 2 | 3-watch | 0-hard | 3 | 0 | 3 | 2 | no | yes | source repair needed |

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
  - source_proxy_only_blocks_runtime_promotion
  - high_MAE_guardrail
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
residual_error_types_found:
  - construction_valueup_false_positive_low_MFE_high_MAE
  - PF_debt_liquidity_orderbook_cashflow_margin_bridge_required
  - large_builder_margin_bridge_gap
  - mid_builder_low_MFE_value_trap
  - source_proxy_runtime_promotion_risk
  - hard_4C_requires_non_price_debt_project_loss_break
new_axis_proposed: false
existing_axis_strengthened:
  - C30_PF_debt_liquidity_orderbook_cashflow_project_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - hard_4C_requires_non_price_thesis_break
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C30_PF_debt_liquidity_orderbook_cashflow_project_margin_bridge_required
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
- scheduled_round / scheduled_loop / large_sector consistency
```

Not validated in this MD:

```text
- primary evidence URL
- exact publication time
- PF refinancing and debt maturity detail
- orderbook quality and cash collection evidence
- project-loss provisioning path
- project-margin conversion
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C30_PF_debt_liquidity_orderbook_cashflow_project_margin_bridge_required,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"Require PF refinancing, debt/liquidity control, orderbook quality, cash-flow and project-margin bridge before clean Stage2/Green","keeps 010780 with local 4B/PF bridge watch; demotes 375500/002990","R10L86-C30-01-S2A-20240125|R10L86-C30-02-S2FP-20240712|R10L86-C30-03-S2FP-20240213",3,3,2,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R10L86-C30-01", "symbol": "010780", "company_name": "아이에스동서", "round": "R10", "loop": 86, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "LARGE_DEVELOPER_BUILDING_MATERIALS_MID_BUILDER_PF_DEBT_ORDERBOOK_CASHFLOW_MARGIN_BRIDGE_VS_VALUEUP_HOUSING_THEME_FADE", "case_type": "developer_building_materials_PF_recovery_positive_with_high_MAE_watch", "positive_or_counterexample": "positive", "best_trigger": "R10L86-C30-01-S2A-20240125", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_MFE_but_high_MAE_PF_orderbook_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_high_MAE_PF_bridge_needed", "price_source": "Songdaiki/stock-web", "notes": "C30 developer positives need PF exposure, debt maturity, orderbook cash-flow, project-loss path and margin bridge before clean Green."}
{"row_type": "trigger", "trigger_id": "R10L86-C30-01-S2A-20240125", "case_id": "R10L86-C30-01", "symbol": "010780", "company_name": "아이에스동서", "round": "R10", "loop": 86, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "LARGE_DEVELOPER_BUILDING_MATERIALS_MID_BUILDER_PF_DEBT_ORDERBOOK_CASHFLOW_MARGIN_BRIDGE_VS_VALUEUP_HOUSING_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|construction_PF_balance_sheet_guardrail|debt_orderbook_cashflow_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-01-25", "evidence_available_at_that_date": "developer / building-materials / housing-PF recovery and balance-sheet normalization proxy; primary PF, debt maturity, orderbook and project-margin evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["PF_refinancing_proxy", "debt_liquidity_proxy", "orderbook_quality_proxy"], "stage3_evidence_fields": ["confirmed_refinancing", "cash_collection", "orderbook_margin_quality", "project_loss_path", "debt_liquidity", "project_margin_bridge"], "stage4b_evidence_fields": ["construction_MFE_without_PF_bridge", "housing_theme_squeeze", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_debt_liquidity_or_project_loss_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/010/010780/2024.csv", "profile_path": "atlas/symbol_profiles/010/010780.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-01-25", "entry_price": 24850, "MFE_30D_pct": 21.93, "MFE_90D_pct": 25.55, "MFE_180D_pct": 25.55, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -1.61, "MAE_90D_pct": -1.61, "MAE_180D_pct": -18.11, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-03-22", "peak_price": 31200, "drawdown_after_peak_pct": -34.78, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.75, "four_b_full_window_peak_proximity": 0.65, "four_b_timing_verdict": "local_4B_watch_after_developer_MFE_if_PF_debt_orderbook_margin_bridge_stalls", "four_b_evidence_type": ["construction_MFE_without_PF_orderbook_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_debt_project_loss_or_margin_break", "trigger_outcome_label": "positive_MFE_but_high_MAE_PF_orderbook_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_high_MAE_PF_bridge_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2011_CA_candidates", "same_entry_group_id": "R10L86-C30-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L86-C30-01", "trigger_id": "R10L86-C30-01-S2A-20240125", "symbol": "010780", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"PF_refinancing_visibility_score": 35, "debt_liquidity_control_score": 35, "orderbook_quality_score": 40, "cash_flow_bridge_score": 35, "project_margin_bridge_score": 35, "loss_provision_risk_score": 50, "balance_sheet_trust_score": 40, "revision_score": 35, "relative_strength_score": 55, "valuation_repricing_score": 50, "execution_risk_score": 60, "source_quality_score": 20, "4B_watch_score": 45, "4C_watch_score": 25}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"PF_refinancing_visibility_score": 35, "debt_liquidity_control_score": 35, "orderbook_quality_score": 40, "cash_flow_bridge_score": 35, "project_margin_bridge_score": 35, "loss_provision_risk_score": 50, "balance_sheet_trust_score": 40, "revision_score": 35, "relative_strength_score": 55, "valuation_repricing_score": 50, "execution_risk_score": 70, "source_quality_score": 10, "4B_watch_score": 80, "4C_watch_score": 25}, "weighted_score_after": 72, "stage_label_after": "Stage2-Actionable + local 4B/PF-orderbook-margin watch", "changed_components": ["PF_refinancing_visibility_score", "debt_liquidity_control_score", "orderbook_quality_score", "cash_flow_bridge_score", "project_margin_bridge_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C30 requires construction/PF MFE to convert into refinancing, debt/liquidity control, orderbook quality, cash collection, project-loss path and margin bridge before clean Stage2/Green; construction value-up MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 25.55, "MAE_90D_pct": -1.61, "score_return_alignment_label": "positive_MFE_but_high_MAE_PF_orderbook_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_high_MAE_PF_bridge_needed"}
{"row_type": "case", "case_id": "R10L86-C30-02", "symbol": "375500", "company_name": "DL이앤씨", "round": "R10", "loop": 86, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "LARGE_DEVELOPER_BUILDING_MATERIALS_MID_BUILDER_PF_DEBT_ORDERBOOK_CASHFLOW_MARGIN_BRIDGE_VS_VALUEUP_HOUSING_THEME_FADE", "case_type": "large_builder_valueup_PF_margin_bridge_gap_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R10L86-C30-02-S2FP-20240712", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "low_MFE_high_MAE_large_builder_valueup_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_high_MAE", "price_source": "Songdaiki/stock-web", "notes": "Large-builder value-up/PF recovery language should remain RiskWatch unless orderbook quality, cash collection, debt liquidity and project-margin bridge are explicit."}
{"row_type": "trigger", "trigger_id": "R10L86-C30-02-S2FP-20240712", "case_id": "R10L86-C30-02", "symbol": "375500", "company_name": "DL이앤씨", "round": "R10", "loop": 86, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "LARGE_DEVELOPER_BUILDING_MATERIALS_MID_BUILDER_PF_DEBT_ORDERBOOK_CASHFLOW_MARGIN_BRIDGE_VS_VALUEUP_HOUSING_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|construction_PF_balance_sheet_guardrail|debt_orderbook_cashflow_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-07-12", "evidence_available_at_that_date": "large builder / housing policy / PF balance-sheet normalization and value-up proxy without confirmed orderbook margin and cash-flow bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["PF_refinancing_proxy", "debt_liquidity_proxy", "orderbook_quality_proxy"], "stage3_evidence_fields": ["confirmed_refinancing", "cash_collection", "orderbook_margin_quality", "project_loss_path", "debt_liquidity", "project_margin_bridge"], "stage4b_evidence_fields": ["construction_MFE_without_PF_bridge", "housing_theme_squeeze", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_debt_liquidity_or_project_loss_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/375/375500/2024.csv", "profile_path": "atlas/symbol_profiles/375/375500.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-12", "entry_price": 33400, "MFE_30D_pct": 7.78, "MFE_90D_pct": 7.78, "MFE_180D_pct": 7.78, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -14.37, "MAE_90D_pct": -14.37, "MAE_180D_pct": -14.37, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-31", "peak_price": 36000, "drawdown_after_peak_pct": -20.56, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "large_builder_valueup_theme_rejected_without_PF_debt_orderbook_margin_bridge", "four_b_evidence_type": ["construction_MFE_without_PF_orderbook_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_debt_project_loss_or_margin_break", "trigger_outcome_label": "low_MFE_high_MAE_large_builder_valueup_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_high_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2022_CA_candidates", "same_entry_group_id": "R10L86-C30-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L86-C30-02", "trigger_id": "R10L86-C30-02-S2FP-20240712", "symbol": "375500", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"PF_refinancing_visibility_score": 10, "debt_liquidity_control_score": 10, "orderbook_quality_score": 10, "cash_flow_bridge_score": 5, "project_margin_bridge_score": 5, "loss_provision_risk_score": 75, "balance_sheet_trust_score": 15, "revision_score": 15, "relative_strength_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 80, "source_quality_score": 15, "4B_watch_score": 75, "4C_watch_score": 45}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"PF_refinancing_visibility_score": 0, "debt_liquidity_control_score": 0, "orderbook_quality_score": 0, "cash_flow_bridge_score": 0, "project_margin_bridge_score": 0, "loss_provision_risk_score": 75, "balance_sheet_trust_score": 15, "revision_score": 15, "relative_strength_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 90, "source_quality_score": 5, "4B_watch_score": 90, "4C_watch_score": 65}, "weighted_score_after": 43, "stage_label_after": "Rejected-Stage2 / Construction-PF value-up RiskWatch", "changed_components": ["PF_refinancing_visibility_score", "debt_liquidity_control_score", "orderbook_quality_score", "cash_flow_bridge_score", "project_margin_bridge_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C30 requires construction/PF MFE to convert into refinancing, debt/liquidity control, orderbook quality, cash collection, project-loss path and margin bridge before clean Stage2/Green; construction value-up MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 7.78, "MAE_90D_pct": -14.37, "score_return_alignment_label": "low_MFE_high_MAE_large_builder_valueup_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_high_MAE"}
{"row_type": "case", "case_id": "R10L86-C30-03", "symbol": "002990", "company_name": "금호건설", "round": "R10", "loop": 86, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "LARGE_DEVELOPER_BUILDING_MATERIALS_MID_BUILDER_PF_DEBT_ORDERBOOK_CASHFLOW_MARGIN_BRIDGE_VS_VALUEUP_HOUSING_THEME_FADE", "case_type": "mid_builder_PF_valueup_low_MFE_high_MAE_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R10L86-C30-03-S2FP-20240213", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "very_low_MFE_deep_MAE_mid_builder_PF_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_high_MAE", "price_source": "Songdaiki/stock-web", "notes": "Mid-builder PF/value-up theme should be rejected unless refinancing, debt liquidity, orderbook margin, cash-flow and project-loss evidence are repaired."}
{"row_type": "trigger", "trigger_id": "R10L86-C30-03-S2FP-20240213", "case_id": "R10L86-C30-03", "symbol": "002990", "company_name": "금호건설", "round": "R10", "loop": 86, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "LARGE_DEVELOPER_BUILDING_MATERIALS_MID_BUILDER_PF_DEBT_ORDERBOOK_CASHFLOW_MARGIN_BRIDGE_VS_VALUEUP_HOUSING_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|construction_PF_balance_sheet_guardrail|debt_orderbook_cashflow_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-02-13", "evidence_available_at_that_date": "mid builder / PF recovery / low-PBR value-up theme proxy without refinancing, orderbook quality, liquidity or project-margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["PF_refinancing_proxy", "debt_liquidity_proxy", "orderbook_quality_proxy"], "stage3_evidence_fields": ["confirmed_refinancing", "cash_collection", "orderbook_margin_quality", "project_loss_path", "debt_liquidity", "project_margin_bridge"], "stage4b_evidence_fields": ["construction_MFE_without_PF_bridge", "housing_theme_squeeze", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_debt_liquidity_or_project_loss_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002990/2024.csv", "profile_path": "atlas/symbol_profiles/002/002990.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-02-13", "entry_price": 5180, "MFE_30D_pct": 0.97, "MFE_90D_pct": 0.97, "MFE_180D_pct": 0.97, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -15.44, "MAE_90D_pct": -26.35, "MAE_180D_pct": -38.61, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-02-19", "peak_price": 5230, "drawdown_after_peak_pct": -39.2, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "mid_builder_PF_theme_rejected_without_refinancing_liquidity_orderbook_margin_bridge", "four_b_evidence_type": ["construction_MFE_without_PF_orderbook_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_debt_project_loss_or_margin_break", "trigger_outcome_label": "very_low_MFE_deep_MAE_mid_builder_PF_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_high_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2013_CA_candidates", "same_entry_group_id": "R10L86-C30-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L86-C30-03", "trigger_id": "R10L86-C30-03-S2FP-20240213", "symbol": "002990", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"PF_refinancing_visibility_score": 10, "debt_liquidity_control_score": 10, "orderbook_quality_score": 10, "cash_flow_bridge_score": 5, "project_margin_bridge_score": 5, "loss_provision_risk_score": 75, "balance_sheet_trust_score": 15, "revision_score": 15, "relative_strength_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 80, "source_quality_score": 15, "4B_watch_score": 75, "4C_watch_score": 45}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"PF_refinancing_visibility_score": 0, "debt_liquidity_control_score": 0, "orderbook_quality_score": 0, "cash_flow_bridge_score": 0, "project_margin_bridge_score": 0, "loss_provision_risk_score": 75, "balance_sheet_trust_score": 15, "revision_score": 15, "relative_strength_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 90, "source_quality_score": 5, "4B_watch_score": 90, "4C_watch_score": 65}, "weighted_score_after": 43, "stage_label_after": "Rejected-Stage2 / Construction-PF value-up RiskWatch", "changed_components": ["PF_refinancing_visibility_score", "debt_liquidity_control_score", "orderbook_quality_score", "cash_flow_bridge_score", "project_margin_bridge_score", "source_quality_score", "4B_watch_score", "4C_watch_score"], "component_delta_explanation": "C30 requires construction/PF MFE to convert into refinancing, debt/liquidity control, orderbook quality, cash collection, project-loss path and margin bridge before clean Stage2/Green; construction value-up MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 0.97, "MAE_90D_pct": -26.35, "score_return_alignment_label": "very_low_MFE_deep_MAE_mid_builder_PF_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_high_MAE"}
{"row_type": "shadow_weight", "axis": "C30_PF_debt_liquidity_orderbook_cashflow_project_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Construction/PF rerating requires refinancing visibility, debt/liquidity control, orderbook quality, cash collection, project-loss path and project-margin bridge; housing/value-up theme MFE without bridge fades into high MAE or low-MFE false positive.", "backtest_effect": "keeps 010780 with local 4B/PF bridge watch; demotes 375500/002990 construction value-up false positives", "trigger_ids": "R10L86-C30-01-S2A-20240125|R10L86-C30-02-S2FP-20240712|R10L86-C30-03-S2FP-20240213", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 2, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R10", "loop": 86, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["construction_valueup_false_positive_low_MFE_high_MAE", "PF_debt_liquidity_orderbook_cashflow_margin_bridge_required", "large_builder_margin_bridge_gap", "mid_builder_low_MFE_value_trap", "source_proxy_runtime_promotion_risk", "hard_4C_requires_non_price_debt_project_loss_break"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C30, test a canonical-archetype guard requiring PF refinancing, debt/liquidity control, orderbook quality, cash-flow and project-margin bridge before clean Stage2/Green. Keep hard 4C blocked unless a non-price debt/project-loss/margin thesis break is confirmed.

## 27. Next Round State

```text
completed_round = R10
completed_loop = 86
next_round = R11
next_loop = 86
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
price_source = Songdaiki/stock-web
```
