# E2R Stock-Web v12 Residual Research — R10 Loop 84 / L9 / C30

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R10",
  "scheduled_loop": 84,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R10",
  "completed_loop": 84,
  "computed_next_round": "R11",
  "computed_next_loop": 84,
  "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING",
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "fine_archetype_id": "MID_BUILDER_PF_REFINANCING_ORDERBOOK_MARGIN_BRIDGE_VS_HOUSING_THEME_SQUEEZE_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "construction_PF_refinancing_balance_sheet_guardrail",
    "orderbook_quality_to_margin_bridge_test",
    "housing_theme_squeeze_vs_stage2_actionable_split",
    "local_4B_timing_after_construction_MFE",
    "hard_4C_non_price_thesis_break_protection",
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
scheduled_loop = 84
allowed_large_sector = L9_CONSTRUCTION_REALESTATE_HOUSING
selected_large_sector = L9_CONSTRUCTION_REALESTATE_HOUSING
selected_canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
computed_next_round = R11
computed_next_loop = 84
round_schedule_status = valid
round_sector_consistency = pass
```

R10 is the construction / real estate / housing round. This run selects C30 and avoids top-covered large builders. The tested mechanism is:

```text
housing / construction / PF recovery headline
→ PF refinancing and debt maturity control
→ orderbook quality and project-loss path
→ cash-flow and project-margin bridge
→ durable rerating or theme-squeeze / high-MAE fade
```

C30 is the part of the map where a building must be inspected from the basement upward. A rebound in the façade is not enough; PF, debt, cash flow, loss provisions and margin carry the load.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C30 top-covered symbols include `047040`, `006360`, `UNKNOWN_SYMBOL`, `294870`, `005960`, and `000720`. This run avoids that top-covered set and uses:

```text
013580 / 계룡건설
004960 / 한신공영
013360 / 일성건설
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
| 013580 | 계룡건설 | `atlas/symbol_profiles/013/013580.json` | old 1999 CA candidate; selected 2024/2025 forward window clean |
| 004960 | 한신공영 | `atlas/symbol_profiles/004/004960.json` | old CA candidates through 2002; selected 2024/2025 forward window clean |
| 013360 | 일성건설 | `atlas/symbol_profiles/013/013360.json` | old CA candidates through 2017; selected 2024 forward window clean |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R10L84-C30-01 | 013580 | 2024-07-12 | 13,730 | 180D | clean | true |
| R10L84-C30-02 | 004960 | 2024-07-12 | 6,460 | 180D | clean | true |
| R10L84-C30-03 | 013360 | 2024-07-12 | 1,343 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | MID_BUILDER_ORDERBOOK_BALANCE_SHEET_RECOVERY | keep Stage2 only with PF exposure, orderbook quality, cash-flow and margin bridge |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | SMALL_MID_BUILDER_PF_HIGH_MAE_RISKWATCH | allow Stage2 only with high-MAE/PF RiskWatch until refinancing and debt bridge are repaired |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | HOUSING_POLICY_THEME_SQUEEZE_FADE | reject or local-4B-watch when price squeeze lacks PF/orderbook/margin evidence at entry |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R10L84-C30-01 | 013580 | 계룡건설 | Stage2-Actionable | 2024-07-12 | 13,730 | 92.64 | -12.75 | current_profile_partially_correct_delayed_4B_watch_needed |
| R10L84-C30-02 | 004960 | 한신공영 | Stage2-Actionable | 2024-07-12 | 6,460 | 17.03 | -10.68 | current_profile_partially_correct_high_MAE_watch_needed |
| R10L84-C30-03 | 013360 | 일성건설 | Stage2-FalsePositive | 2024-07-12 | 1,343 | 38.5 | -5.44 | current_profile_false_positive_theme_squeeze |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 2
counterexample_count = 1
4B_or_4C_case_count = 3
calibration_usable_case_count = 3
new_independent_case_count = 3
```

## 9. Evidence Source Map

All selected evidence is currently `source_proxy_only=true / evidence_url_pending=true`.

This MD therefore creates a source-repair queue and a C30 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: PF refinancing, debt maturity, cash-flow bridge, orderbook quality, project-loss provisioning, project-margin bridge, company disclosure, filing or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 013580 | `atlas/ohlcv_tradable_by_symbol_year/013/013580/2024.csv` and `2025.csv` | `atlas/symbol_profiles/013/013580.json` |
| 004960 | `atlas/ohlcv_tradable_by_symbol_year/004/004960/2024.csv` and `2025.csv` | `atlas/symbol_profiles/004/004960.json` |
| 013360 | `atlas/ohlcv_tradable_by_symbol_year/013/013360/2024.csv` | `atlas/symbol_profiles/013/013360.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 013580 / 계룡건설

C30 delayed recovery positive. The 30D/90D windows were only moderate, but the 180D path eventually produced a strong rerating. This is useful evidence that some mid-builder recovery cases should not be rejected too early. However, the Stage2 label remains conditional on PF exposure, debt maturity, orderbook quality and project-margin repair.

### Case 2 — 004960 / 한신공영

C30 bounded recovery positive with high-MAE/PF RiskWatch. The early MFE was useful, but it faded and the 180D MAE widened. This is a classic “right enough to watch, not clean enough to Green” case.

### Case 3 — 013360 / 일성건설

C30 housing-policy squeeze false positive. The MFE was large, but the evidence bridge is weak and the post-peak drawdown was fast. A theme squeeze does not prove PF refinancing, orderbook quality or margin conversion.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 013580 | 13,730 | 13.47 | -3.79 | 13.47 | -3.79 | 92.64 | -12.75 | 2025-04-10 / 26,450 | -21.93 |
| 004960 | 6,460 | 17.03 | -4.64 | 17.03 | -4.64 | 17.03 | -10.68 | 2024-07-31 / 7,560 | -23.68 |
| 013360 | 1,343 | 38.50 | -4.10 | 38.50 | -5.44 | 38.50 | -5.44 | 2024-07-23 / 1,860 | -31.72 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R10L84-C30-01 | Stage2-Actionable if PF/orderbook bridge exists | delayed large MFE, interim MAE | partially correct; delayed 4B watch needed |
| R10L84-C30-02 | Stage2-Actionable if small-builder recovery is over-credited | bounded MFE, later fade | high-MAE/PF RiskWatch needed |
| R10L84-C30-03 | risk of treating housing-policy squeeze as Stage2 | fast MFE and fast drawdown | false positive / theme squeeze |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C30, the residual is not Green lateness. The residual is whether construction/PF MFE becomes clean Stage2/Green before refinancing, debt/liquidity, orderbook quality and project-margin bridge are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R10L84-C30-01 | 0.82 | 0.72 | local 4B watch after delayed construction MFE if PF/margin bridge stalls |
| R10L84-C30-02 | 0.82 | 0.72 | local 4B and PF RiskWatch when recovery MFE outruns evidence |
| R10L84-C30-03 | 0.30 | 0.25 | housing theme squeeze rejected without PF/orderbook/margin bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_debt_project_loss_break
hard_4c_price_only_allowed = false
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L9/C30 construction rows need PF refinancing, debt/liquidity control, orderbook quality and project-margin bridge before clean Stage2/Green
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
candidate_axis = C30_PF_debt_orderbook_project_margin_bridge_required
effect = keep bridge-positive recovery cases with local 4B/high-MAE watch; demote housing-theme squeeze false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 23.00 | -4.62 | may over-credit construction/PF theme MFE | needs C30 bridge repair |
| P1 canonical shadow bridge profile | 3 | 15.25 on kept positives at 90D, 54.84 at 180D | keeps positives under RiskWatch | demotes 013360 theme squeeze | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R10L84-C30-01 | 76 | Stage2-Actionable | 75 | Stage2-Actionable + local 4B/high-MAE watch | partially aligned |
| R10L84-C30-02 | 76 | Stage2-Actionable | 72 | Stage2-Actionable + high-MAE/PF RiskWatch | partially aligned |
| R10L84-C30-03 | 58 | Stage2-Watch/FalsePositive | 45 | Rejected-Stage2 / Theme-squeeze RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | MID_BUILDER_PF_REFINANCING_ORDERBOOK_MARGIN_BRIDGE_VS_HOUSING_THEME_SQUEEZE_FADE | 2 | 1 | 3-watch | 0 | 3 | 0 | 3 | 2 | no | yes | source repair needed |

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
residual_error_types_found:
  - housing_theme_squeeze_false_positive
  - PF_debt_orderbook_project_margin_bridge_required
  - local_4B_late_after_construction_MFE
  - source_proxy_runtime_promotion_risk
  - high_MAE_positive_Green_blocker
new_axis_proposed: false
existing_axis_strengthened:
  - C30_PF_debt_orderbook_project_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - high_MAE_blocks_clean_Green
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C30_PF_debt_orderbook_project_margin_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent cases, 1 counterexample, and 2 residual errors for R10/L9_CONSTRUCTION_REALESTATE_HOUSING/C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK.

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
- orderbook quality and project margin
- project-loss provisioning path
- cash-flow bridge
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C30_PF_debt_orderbook_project_margin_bridge_required,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"Require PF refinancing, debt/liquidity control, orderbook quality, project-loss visibility and project-margin bridge before clean Stage2/Green","keeps 013580/004960 with local 4B or high-MAE RiskWatch; demotes 013360","R10L84-C30-01-S2A-20240712|R10L84-C30-02-S2A-20240712|R10L84-C30-03-S2FP-20240712",3,3,1,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R10L84-C30-01", "symbol": "013580", "company_name": "계룡건설", "round": "R10", "loop": 84, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_PF_REFINANCING_ORDERBOOK_MARGIN_BRIDGE_VS_HOUSING_THEME_SQUEEZE_FADE", "case_type": "mid_builder_orderbook_balance_sheet_recovery_positive_with_delayed_MFE", "positive_or_counterexample": "positive", "best_trigger": "R10L84-C30-01-S2A-20240712", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "delayed_positive_MFE_but_requires_PF_margin_bridge_and_local_4B_watch", "current_profile_verdict": "current_profile_partially_correct_delayed_4B_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C30 can keep Stage2 only when PF exposure, debt maturity, orderbook quality, project-loss risk and margin bridge are visible."}
{"row_type": "trigger", "trigger_id": "R10L84-C30-01-S2A-20240712", "case_id": "R10L84-C30-01", "symbol": "013580", "company_name": "계룡건설", "round": "R10", "loop": 84, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_PF_REFINANCING_ORDERBOOK_MARGIN_BRIDGE_VS_HOUSING_THEME_SQUEEZE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|construction_PF_balance_sheet_guardrail|housing_theme_squeeze_vs_stage2_split|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-12", "evidence_available_at_that_date": "mid-builder orderbook / PF risk normalization / balance-sheet recovery proxy; primary PF-refinancing and project-margin evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["PF_refinancing_proxy", "orderbook_quality_proxy", "project_margin_proxy", "debt_liquidity_proxy"], "stage3_evidence_fields": ["confirmed_refinancing", "cash_flow_bridge", "loss_provision_path", "orderbook_margin_quality", "balance_sheet_trust"], "stage4b_evidence_fields": ["housing_theme_MFE_without_PF_bridge", "post_peak_drawdown", "balance_sheet_risk"], "stage4c_evidence_fields": ["hard_debt_liquidity_or_project_loss_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/013/013580/2024.csv", "profile_path": "atlas/symbol_profiles/013/013580.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-12", "entry_price": 13730, "MFE_30D_pct": 13.47, "MFE_90D_pct": 13.47, "MFE_180D_pct": 92.64, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -3.79, "MAE_90D_pct": -3.79, "MAE_180D_pct": -12.75, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-04-10", "peak_price": 26450, "drawdown_after_peak_pct": -21.93, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.82, "four_b_full_window_peak_proximity": 0.72, "four_b_timing_verdict": "local_4B_watch_after_delayed_construction_MFE_if_PF_margin_bridge_stalls", "four_b_evidence_type": ["housing_or_construction_MFE_without_PF_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_debt_project_loss_break", "trigger_outcome_label": "delayed_positive_MFE_but_requires_PF_margin_bridge_and_local_4B_watch", "current_profile_verdict": "current_profile_partially_correct_delayed_4B_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_2025_window_after_old_1999_CA_candidate", "same_entry_group_id": "R10L84-C30-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L84-C30-01", "trigger_id": "R10L84-C30-01-S2A-20240712", "symbol": "013580", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"PF_refinancing_visibility_score": 35, "debt_liquidity_control_score": 35, "orderbook_quality_score": 45, "project_margin_bridge_score": 35, "cash_flow_bridge_score": 30, "balance_sheet_trust_score": 40, "loss_provision_risk_score": 45, "revision_score": 35, "relative_strength_score": 45, "valuation_repricing_score": 50, "execution_risk_score": 45, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"PF_refinancing_visibility_score": 35, "debt_liquidity_control_score": 35, "orderbook_quality_score": 45, "project_margin_bridge_score": 35, "cash_flow_bridge_score": 30, "balance_sheet_trust_score": 40, "loss_provision_risk_score": 45, "revision_score": 35, "relative_strength_score": 45, "valuation_repricing_score": 50, "execution_risk_score": 45, "source_quality_score": 10, "4B_watch_score": 80}, "weighted_score_after": 75, "stage_label_after": "Stage2-Actionable + local 4B/high-MAE watch", "changed_components": ["PF_refinancing_visibility_score", "debt_liquidity_control_score", "project_margin_bridge_score", "cash_flow_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C30 requires PF refinancing, debt/liquidity control, orderbook quality, project-loss path and margin bridge before clean Stage2/Green; housing/construction theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 13.47, "MAE_90D_pct": -3.79, "score_return_alignment_label": "delayed_positive_MFE_but_requires_PF_margin_bridge_and_local_4B_watch", "current_profile_verdict": "current_profile_partially_correct_delayed_4B_watch_needed"}
{"row_type": "case", "case_id": "R10L84-C30-02", "symbol": "004960", "company_name": "한신공영", "round": "R10", "loop": 84, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_PF_REFINANCING_ORDERBOOK_MARGIN_BRIDGE_VS_HOUSING_THEME_SQUEEZE_FADE", "case_type": "small_mid_builder_recovery_positive_but_PF_high_MAE_RiskWatch", "positive_or_counterexample": "positive", "best_trigger": "R10L84-C30-02-S2A-20240712", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "bounded_MFE_with_later_fade_requires_high_MAE_RiskWatch", "current_profile_verdict": "current_profile_partially_correct_high_MAE_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "Small/mid builder rebound can be Stage2 only with high-MAE/PF RiskWatch until refinancing, cash-flow and project-margin evidence is repaired."}
{"row_type": "trigger", "trigger_id": "R10L84-C30-02-S2A-20240712", "case_id": "R10L84-C30-02", "symbol": "004960", "company_name": "한신공영", "round": "R10", "loop": 84, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_PF_REFINANCING_ORDERBOOK_MARGIN_BRIDGE_VS_HOUSING_THEME_SQUEEZE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|construction_PF_balance_sheet_guardrail|housing_theme_squeeze_vs_stage2_split|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-12", "evidence_available_at_that_date": "small/mid builder recovery and orderbook normalization proxy; primary debt/PF/project-margin evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["PF_refinancing_proxy", "orderbook_quality_proxy", "project_margin_proxy", "debt_liquidity_proxy"], "stage3_evidence_fields": ["confirmed_refinancing", "cash_flow_bridge", "loss_provision_path", "orderbook_margin_quality", "balance_sheet_trust"], "stage4b_evidence_fields": ["housing_theme_MFE_without_PF_bridge", "post_peak_drawdown", "balance_sheet_risk"], "stage4c_evidence_fields": ["hard_debt_liquidity_or_project_loss_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/004/004960/2024.csv", "profile_path": "atlas/symbol_profiles/004/004960.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-12", "entry_price": 6460, "MFE_30D_pct": 17.03, "MFE_90D_pct": 17.03, "MFE_180D_pct": 17.03, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.64, "MAE_90D_pct": -4.64, "MAE_180D_pct": -10.68, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-31", "peak_price": 7560, "drawdown_after_peak_pct": -23.68, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.82, "four_b_full_window_peak_proximity": 0.72, "four_b_timing_verdict": "local_4B_and_PF_RiskWatch_needed_when_recovery_MFE_outruns_debt_margin_bridge", "four_b_evidence_type": ["housing_or_construction_MFE_without_PF_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_debt_project_loss_break", "trigger_outcome_label": "bounded_MFE_with_later_fade_requires_high_MAE_RiskWatch", "current_profile_verdict": "current_profile_partially_correct_high_MAE_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_2025_window_after_old_2002_CA_candidates", "same_entry_group_id": "R10L84-C30-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L84-C30-02", "trigger_id": "R10L84-C30-02-S2A-20240712", "symbol": "004960", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"PF_refinancing_visibility_score": 35, "debt_liquidity_control_score": 35, "orderbook_quality_score": 45, "project_margin_bridge_score": 35, "cash_flow_bridge_score": 30, "balance_sheet_trust_score": 40, "loss_provision_risk_score": 45, "revision_score": 35, "relative_strength_score": 45, "valuation_repricing_score": 50, "execution_risk_score": 55, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"PF_refinancing_visibility_score": 35, "debt_liquidity_control_score": 35, "orderbook_quality_score": 45, "project_margin_bridge_score": 35, "cash_flow_bridge_score": 30, "balance_sheet_trust_score": 40, "loss_provision_risk_score": 45, "revision_score": 35, "relative_strength_score": 45, "valuation_repricing_score": 50, "execution_risk_score": 70, "source_quality_score": 10, "4B_watch_score": 80}, "weighted_score_after": 72, "stage_label_after": "Stage2-Actionable + local 4B/high-MAE watch", "changed_components": ["PF_refinancing_visibility_score", "debt_liquidity_control_score", "project_margin_bridge_score", "cash_flow_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C30 requires PF refinancing, debt/liquidity control, orderbook quality, project-loss path and margin bridge before clean Stage2/Green; housing/construction theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 17.03, "MAE_90D_pct": -4.64, "score_return_alignment_label": "bounded_MFE_with_later_fade_requires_high_MAE_RiskWatch", "current_profile_verdict": "current_profile_partially_correct_high_MAE_watch_needed"}
{"row_type": "case", "case_id": "R10L84-C30-03", "symbol": "013360", "company_name": "일성건설", "round": "R10", "loop": 84, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_PF_REFINANCING_ORDERBOOK_MARGIN_BRIDGE_VS_HOUSING_THEME_SQUEEZE_FADE", "case_type": "housing_policy_theme_squeeze_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R10L84-C30-03-S2FP-20240712", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "theme_squeeze_MFE_not_valid_stage2_without_PF_margin_bridge", "current_profile_verdict": "current_profile_false_positive_theme_squeeze", "price_source": "Songdaiki/stock-web", "notes": "Housing/construction squeeze after theme flow should not validate Stage2 unless PF/debt/orderbook/margin evidence existed at entry."}
{"row_type": "trigger", "trigger_id": "R10L84-C30-03-S2FP-20240712", "case_id": "R10L84-C30-03", "symbol": "013360", "company_name": "일성건설", "round": "R10", "loop": 84, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "MID_BUILDER_PF_REFINANCING_ORDERBOOK_MARGIN_BRIDGE_VS_HOUSING_THEME_SQUEEZE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|construction_PF_balance_sheet_guardrail|housing_theme_squeeze_vs_stage2_split|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-07-12", "evidence_available_at_that_date": "housing/construction policy-theme squeeze proxy without PF refinancing, orderbook quality, project-margin or balance-sheet repair bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["PF_refinancing_proxy", "orderbook_quality_proxy", "project_margin_proxy", "debt_liquidity_proxy"], "stage3_evidence_fields": ["confirmed_refinancing", "cash_flow_bridge", "loss_provision_path", "orderbook_margin_quality", "balance_sheet_trust"], "stage4b_evidence_fields": ["housing_theme_MFE_without_PF_bridge", "post_peak_drawdown", "balance_sheet_risk"], "stage4c_evidence_fields": ["hard_debt_liquidity_or_project_loss_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/013/013360/2024.csv", "profile_path": "atlas/symbol_profiles/013/013360.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-12", "entry_price": 1343, "MFE_30D_pct": 38.5, "MFE_90D_pct": 38.5, "MFE_180D_pct": 38.5, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -4.1, "MAE_90D_pct": -5.44, "MAE_180D_pct": -5.44, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-23", "peak_price": 1860, "drawdown_after_peak_pct": -31.72, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.3, "four_b_full_window_peak_proximity": 0.25, "four_b_timing_verdict": "theme_squeeze_rejected_or_local_4B_watch_without_PF_orderbook_margin_bridge", "four_b_evidence_type": ["housing_or_construction_MFE_without_PF_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_debt_project_loss_break", "trigger_outcome_label": "theme_squeeze_MFE_not_valid_stage2_without_PF_margin_bridge", "current_profile_verdict": "current_profile_false_positive_theme_squeeze", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2017_CA_candidate", "same_entry_group_id": "R10L84-C30-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L84-C30-03", "trigger_id": "R10L84-C30-03-S2FP-20240712", "symbol": "013360", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"PF_refinancing_visibility_score": 5, "debt_liquidity_control_score": 10, "orderbook_quality_score": 10, "project_margin_bridge_score": 5, "cash_flow_bridge_score": 5, "balance_sheet_trust_score": 15, "loss_provision_risk_score": 75, "revision_score": 15, "relative_strength_score": 60, "valuation_repricing_score": 35, "execution_risk_score": 80, "source_quality_score": 15, "4B_watch_score": 75}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"PF_refinancing_visibility_score": 0, "debt_liquidity_control_score": 0, "orderbook_quality_score": 10, "project_margin_bridge_score": 0, "cash_flow_bridge_score": 0, "balance_sheet_trust_score": 15, "loss_provision_risk_score": 75, "revision_score": 15, "relative_strength_score": 60, "valuation_repricing_score": 35, "execution_risk_score": 90, "source_quality_score": 5, "4B_watch_score": 85}, "weighted_score_after": 45, "stage_label_after": "Rejected-Stage2 / Theme-squeeze RiskWatch", "changed_components": ["PF_refinancing_visibility_score", "debt_liquidity_control_score", "project_margin_bridge_score", "cash_flow_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C30 requires PF refinancing, debt/liquidity control, orderbook quality, project-loss path and margin bridge before clean Stage2/Green; housing/construction theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 38.5, "MAE_90D_pct": -5.44, "score_return_alignment_label": "theme_squeeze_MFE_not_valid_stage2_without_PF_margin_bridge", "current_profile_verdict": "current_profile_false_positive_theme_squeeze"}
{"row_type": "shadow_weight", "axis": "C30_PF_debt_orderbook_project_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Construction/PF rerating requires PF refinancing, debt/liquidity control, orderbook quality, project-loss visibility and project-margin bridge; housing theme or short squeeze MFE without bridge is not clean Stage2/Green.", "backtest_effect": "keeps 013580/004960 with local 4B or high-MAE RiskWatch; demotes 013360 theme-squeeze false positive", "trigger_ids": "R10L84-C30-01-S2A-20240712|R10L84-C30-02-S2A-20240712|R10L84-C30-03-S2FP-20240712", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 1, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R10", "loop": 84, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail"], "residual_error_types_found": ["housing_theme_squeeze_false_positive", "PF_debt_orderbook_project_margin_bridge_required", "local_4B_late_after_construction_MFE", "source_proxy_runtime_promotion_risk", "high_MAE_positive_Green_blocker"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C30, test a canonical-archetype guard requiring PF refinancing, debt/liquidity control, orderbook quality, project-loss path and project-margin bridge before clean Stage2/Green.

## 27. Next Round State

```text
completed_round = R10
completed_loop = 84
next_round = R11
next_loop = 84
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
price_source = Songdaiki/stock-web
```
