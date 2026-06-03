# E2R Stock-Web v12 Residual Research — R1 Loop 84 / L1 / C05

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R1",
  "scheduled_loop": 84,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R1",
  "completed_loop": 84,
  "computed_next_round": "R2",
  "computed_next_loop": 84,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP",
  "fine_archetype_id": "ENGINEERING_DESIGN_OVERSEAS_INFRA_CONTRACT_MARGIN_BRIDGE_VS_RECONSTRUCTION_THEME_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "under_covered_C05_axis",
    "counterexample_mining",
    "EPC_engineering_contract_margin_gap_guardrail",
    "theme_headline_vs_margin_bridge_test",
    "4B_non_price_requirement_stress_test",
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
scheduled_round = R1
scheduled_loop = 84
allowed_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
computed_next_round = R2
computed_next_loop = 84
round_schedule_status = valid
round_sector_consistency = pass
```

R1 begins loop84 after loop83 R13 completed. This run selects C05 because the No-Repeat coverage table shows C05 remains thin relative to the more crowded C02/C03/C04 axes.

The tested mechanism:

```text
EPC / engineering / design / project-management contract headline
→ named contract or project scope
→ backlog / fee duration / client quality
→ cost pass-through and working-capital risk
→ gross-margin / OP bridge
→ durable rerating or theme fade
```

C05 is not “big infrastructure word appears.” It is a bridge inspection. The contract headline is the ribbon-cutting; margin conversion is the concrete setting underneath.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C05 top-covered symbols include `006360`, `047040`, `000720`, `028050`, `375500`, and `034300`. This run avoids that top-covered set and uses:

```text
053690 / 한미글로벌
054930 / 유신
002150 / 도화엔지니어링
023350 / 한국종합기술
```

All four are treated as new independent C05 engineering/EPC-margin-gap cases for this loop. No hard duplicate is intentionally reused.

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
| 053690 | 한미글로벌 | `atlas/symbol_profiles/053/053690.json` | no profile-level CA candidate |
| 054930 | 유신 | `atlas/symbol_profiles/054/054930.json` | old 2002~2003 CA candidates; selected 2024/2025 forward window clean |
| 002150 | 도화엔지니어링 | `atlas/symbol_profiles/002/002150.json` | old 2013 CA candidates; selected 2024/2025 forward window clean |
| 023350 | 한국종합기술 | `atlas/symbol_profiles/023/023350.json` | no profile-level CA candidate |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R1L84-C05-01 | 053690 | 2024-07-12 | 16,690 | 180D | clean | true |
| R1L84-C05-02 | 054930 | 2024-07-12 | 26,750 | 180D | clean | true |
| R1L84-C05-03 | 002150 | 2024-07-12 | 7,460 | 180D | clean | true |
| R1L84-C05-04 | 023350 | 2024-07-12 | 5,390 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | PROJECT_MANAGEMENT_BACKLOG_FEE_MARGIN_BRIDGE | keep Stage2 only with named contract, fee duration, client quality and margin bridge |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | ENGINEERING_RECONSTRUCTION_THEME_FADE | reject or demote when the move is reconstruction / infrastructure theme without contract economics |
| C05_EPC_MEGA_CONTRACT_MARGIN_GAP | DELAYED_MICROCAP_SQUEEZE_NOT_ORIGINAL_STAGE2 | delayed squeeze after high MAE does not validate original trigger without entry-date evidence |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R1L84-C05-01 | 053690 | 한미글로벌 | Stage2-Actionable | 2024-07-12 | 16,690 | 16.84 | -18.93 | current_profile_partially_correct_high_MAE_watch_needed |
| R1L84-C05-02 | 054930 | 유신 | Stage2-FalsePositive | 2024-07-12 | 26,750 | 17.57 | -27.1 | current_profile_false_positive_4B_too_late |
| R1L84-C05-03 | 002150 | 도화엔지니어링 | Stage2-FalsePositive | 2024-07-12 | 7,460 | 10.99 | -17.56 | current_profile_false_positive |
| R1L84-C05-04 | 023350 | 한국종합기술 | Stage2-FalsePositive | 2024-07-12 | 5,390 | 15.77 | -17.99 | current_profile_false_positive_delayed_squeeze |

## 8. Positive vs Counterexample Balance

```text
positive_case_count = 1
counterexample_count = 3
4B_or_4C_case_count = 3
calibration_usable_case_count = 4
new_independent_case_count = 4
```

## 9. Evidence Source Map

All selected evidence is currently `source_proxy_only=true / evidence_url_pending=true`.

This MD therefore creates a source-repair queue and a C05 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: contract disclosure, company IR, project award, client name, project duration, contract amount, cost pass-through, working-capital burden, backlog conversion, or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 053690 | `atlas/ohlcv_tradable_by_symbol_year/053/053690/2024.csv` and `2025.csv` | `atlas/symbol_profiles/053/053690.json` |
| 054930 | `atlas/ohlcv_tradable_by_symbol_year/054/054930/2024.csv` and `2025.csv` | `atlas/symbol_profiles/054/054930.json` |
| 002150 | `atlas/ohlcv_tradable_by_symbol_year/002/002150/2024.csv` and `2025.csv` | `atlas/symbol_profiles/002/002150.json` |
| 023350 | `atlas/ohlcv_tradable_by_symbol_year/023/023350/2024.csv` and `2025.csv` | `atlas/symbol_profiles/023/023350.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 053690 / 한미글로벌

C05 bounded positive with high-MAE watch. The price path eventually produced useful MFE, but the deep interim MAE means it cannot be treated as a clean Green-style engineering winner. It needs a local 4B / RiskWatch wrapper unless source repair proves fee backlog, client durability, cost pass-through and margin conversion.

### Case 2 — 054930 / 유신

C05 theme-spike false positive. The stock produced a sharp theme MFE but then gave back enough to make the initial Stage2-Actionable label unsafe. This is the clearest example that reconstruction / engineering heat is not the same as contract-margin evidence.

### Case 3 — 002150 / 도화엔지니어링

C05 low-quality MFE false positive. The short MFE is too small relative to the MAE unless the source repair pass attaches a real contract and margin bridge.

### Case 4 — 023350 / 한국종합기술

C05 delayed squeeze false positive. A later squeeze-like recovery does not validate the original July trigger because the initial path produced high MAE and lacked entry-date contract economics.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 053690 | 16,690 | 15.52 | -17.62 | 15.52 | -17.62 | 16.84 | -18.93 | 2025-02-13 / 19,500 | -30.62 |
| 054930 | 26,750 | 17.57 | -24.86 | 17.57 | -24.86 | 17.57 | -27.10 | 2024-07-25 / 31,450 | -37.99 |
| 002150 | 7,460 | 10.99 | -14.88 | 10.99 | -14.88 | 10.99 | -17.56 | 2024-07-25 / 8,280 | -25.72 |
| 023350 | 5,390 | 3.34 | -17.99 | 3.34 | -17.99 | 15.77 | -17.99 | 2025-04-07 / 6,240 | -20.67 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R1L84-C05-01 | Stage2-Actionable if contract/margin bridge exists | useful MFE but high MAE | partially correct; high-MAE/local 4B watch needed |
| R1L84-C05-02 | risk of treating engineering/reconstruction theme as Stage2 | high MFE and very high MAE | false positive / 4B too late |
| R1L84-C05-03 | risk of treating civil-engineering theme as Stage2 | small MFE / high MAE | false positive |
| R1L84-C05-04 | risk of validating delayed squeeze | early high MAE, late bounce | false positive / delayed squeeze |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C05, the residual is not Green lateness. The residual is whether a contract / infrastructure / reconstruction headline is allowed to become Stage2-Actionable before backlog duration, cost pass-through and margin conversion are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R1L84-C05-01 | 0.80 | 0.70 | local 4B watch after contract-theme MFE if margin bridge stalls |
| R1L84-C05-02 | 0.80 | 0.70 | theme MFE should be local 4B watch or reject without contract bridge |
| R1L84-C05-03 | 0.35 | 0.30 | short theme MFE rejected without orderbook/margin bridge |
| R1L84-C05-04 | 0.35 | 0.30 | delayed squeeze not valid Stage2 without entry-date bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_project_loss_or_contract_break
hard_4c_price_only_allowed = false
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = R1 engineering/EPC rows need named contract, backlog/fee duration, cost pass-through and margin bridge before Stage2-Actionable
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C05_EPC_MEGA_CONTRACT_MARGIN_GAP
candidate_axis = C05_engineering_EPC_contract_backlog_margin_bridge_required
effect = keep one bounded positive only with high-MAE/local 4B watch; demote theme false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 4 | 11.86 | -18.84 | may over-credit engineering/reconstruction theme | needs C05 bridge repair |
| P1 canonical shadow bridge profile | 4 | 15.52 on kept positive | -17.62 on kept positive | demotes 054930/002150/023350 | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R1L84-C05-01 | 76 | Stage2-Actionable | 78 | Stage2-Actionable + high-MAE/local 4B watch | partially aligned |
| R1L84-C05-02 | 58 | Stage2-Watch/FalsePositive | 47 | Rejected-Stage2 / RiskWatch | improved |
| R1L84-C05-03 | 58 | Stage2-Watch/FalsePositive | 47 | Rejected-Stage2 / RiskWatch | improved |
| R1L84-C05-04 | 58 | Stage2-Watch/FalsePositive | 47 | Rejected-Stage2 / RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C05_EPC_MEGA_CONTRACT_MARGIN_GAP | ENGINEERING_DESIGN_OVERSEAS_INFRA_CONTRACT_MARGIN_BRIDGE_VS_RECONSTRUCTION_THEME_FADE | 1 | 3 | 3-watch | 0 | 4 | 0 | 4 | 3 | no | yes | source repair needed |

## 22. Residual Contribution Summary

```text
new_independent_case_count: 4
reused_case_count: 0
reused_case_ids: []
new_symbol_count: 4
new_canonical_archetype_count: 0
new_fine_archetype_count: 1
new_trigger_family_count: 4
tested_existing_calibrated_axes:
  - stage2_actionable_evidence_bonus
  - price_only_blowoff_blocks_positive_stage
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
  - source_proxy_only_blocks_runtime_promotion
  - high_MAE_guardrail
residual_error_types_found:
  - engineering_contract_theme_false_positive_high_MAE
  - EPC_margin_bridge_required
  - source_proxy_runtime_promotion_risk
  - local_4B_needed_after_contract_theme_MFE
  - delayed_squeeze_not_original_stage2_validation
new_axis_proposed: false
existing_axis_strengthened:
  - C05_engineering_EPC_contract_backlog_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - high_MAE_blocks_clean_Green
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C05_engineering_EPC_contract_backlog_margin_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 4 new independent cases, 3 counterexamples, and 3 residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C05_EPC_MEGA_CONTRACT_MARGIN_GAP.

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
- named contract amount and client
- backlog duration / fee schedule
- cost pass-through and working-capital detail
- gross-margin / OP conversion
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C05_engineering_EPC_contract_backlog_margin_bridge_required,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C05_EPC_MEGA_CONTRACT_MARGIN_GAP,0,1,+1,"Require named EPC/engineering contract economics, backlog/fee duration, cost pass-through and margin bridge before Stage2-Actionable","keeps 053690 only with high-MAE/local 4B watch; demotes 054930/002150/023350","R1L84-C05-01-S2A-20240712|R1L84-C05-02-S2FP-20240712|R1L84-C05-03-S2FP-20240712|R1L84-C05-04-S2FP-20240712",4,4,3,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R1L84-C05-01", "symbol": "053690", "company_name": "한미글로벌", "round": "R1", "loop": 84, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "ENGINEERING_DESIGN_OVERSEAS_INFRA_CONTRACT_MARGIN_BRIDGE_VS_RECONSTRUCTION_THEME_FADE", "case_type": "project_management_engineering_positive_with_high_MAE_watch", "positive_or_counterexample": "positive", "best_trigger": "R1L84-C05-01-S2A-20240712", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "bounded_positive_high_MAE_local_4B_watch", "current_profile_verdict": "current_profile_partially_correct_high_MAE_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "Project-management or EPC engineering positives need visible fee backlog, contract duration, cost pass-through and margin conversion."}
{"row_type": "trigger", "trigger_id": "R1L84-C05-01-S2A-20240712", "case_id": "R1L84-C05-01", "symbol": "053690", "company_name": "한미글로벌", "round": "R1", "loop": 84, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "ENGINEERING_DESIGN_OVERSEAS_INFRA_CONTRACT_MARGIN_BRIDGE_VS_RECONSTRUCTION_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|EPC_engineering_contract_margin_gap_guardrail|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-12", "evidence_available_at_that_date": "overseas infrastructure/project-management order pipeline proxy; backlog-to-fee-margin bridge pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["named_contract_or_policy_project_proxy", "backlog_or_fee_visibility_proxy", "margin_bridge_proxy"], "stage3_evidence_fields": ["contract_duration", "cost_pass_through", "gross_margin_conversion", "revision_confirmation"], "stage4b_evidence_fields": ["theme_MFE_without_contract_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_project_loss_or_contract_cancellation_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/053/053690/2024.csv", "profile_path": "atlas/symbol_profiles/053/053690.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-12", "entry_price": 16690, "MFE_30D_pct": 15.52, "MFE_90D_pct": 15.52, "MFE_180D_pct": 16.84, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -17.62, "MAE_90D_pct": -17.62, "MAE_180D_pct": -18.93, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-13", "peak_price": 19500, "drawdown_after_peak_pct": -30.62, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.8, "four_b_full_window_peak_proximity": 0.7, "four_b_timing_verdict": "local_4B_watch_after_contract_theme_MFE_if_margin_bridge_stalls", "four_b_evidence_type": ["theme_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_project_loss_or_contract_break", "trigger_outcome_label": "bounded_positive_high_MAE_local_4B_watch", "current_profile_verdict": "current_profile_partially_correct_high_MAE_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_profile_CA_candidate", "same_entry_group_id": "R1L84-C05-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L84-C05-01", "trigger_id": "R1L84-C05-01-S2A-20240712", "symbol": "053690", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "raw_component_scores_before": {"contract_score": 35, "backlog_visibility_score": 35, "margin_bridge_score": 30, "revision_score": 35, "relative_strength_score": 50, "customer_quality_score": 35, "policy_or_regulatory_score": 20, "valuation_repricing_score": 45, "execution_risk_score": 50, "cost_pass_through_score": 30, "project_duration_visibility_score": 35, "source_quality_score": 20}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"contract_score": 35, "backlog_visibility_score": 35, "margin_bridge_score": 35, "revision_score": 35, "relative_strength_score": 50, "customer_quality_score": 35, "policy_or_regulatory_score": 20, "valuation_repricing_score": 45, "execution_risk_score": 55, "cost_pass_through_score": 30, "project_duration_visibility_score": 35, "source_quality_score": 10}, "weighted_score_after": 78, "stage_label_after": "Stage2-Actionable + high-MAE/local 4B watch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "cost_pass_through_score", "source_quality_score", "execution_risk_score"], "component_delta_explanation": "C05 requires named EPC/engineering contract economics, backlog/fee duration, cost pass-through and margin bridge before Stage2-Actionable; reconstruction/theme MFE alone is demoted.", "MFE_90D_pct": 15.52, "MAE_90D_pct": -17.62, "score_return_alignment_label": "bounded_positive_high_MAE_local_4B_watch", "current_profile_verdict": "current_profile_partially_correct_high_MAE_watch_needed"}
{"row_type": "case", "case_id": "R1L84-C05-02", "symbol": "054930", "company_name": "유신", "round": "R1", "loop": 84, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "ENGINEERING_DESIGN_OVERSEAS_INFRA_CONTRACT_MARGIN_BRIDGE_VS_RECONSTRUCTION_THEME_FADE", "case_type": "engineering_reconstruction_theme_MFE_fade", "positive_or_counterexample": "counterexample", "best_trigger": "R1L84-C05-02-S2FP-20240712", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "theme_spike_high_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_4B_too_late", "price_source": "Songdaiki/stock-web", "notes": "Design/engineering theme MFE is not C05 Stage2 unless named contract, fee visibility and margin pass-through are verified."}
{"row_type": "trigger", "trigger_id": "R1L84-C05-02-S2FP-20240712", "case_id": "R1L84-C05-02", "symbol": "054930", "company_name": "유신", "round": "R1", "loop": 84, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "ENGINEERING_DESIGN_OVERSEAS_INFRA_CONTRACT_MARGIN_BRIDGE_VS_RECONSTRUCTION_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|EPC_engineering_contract_margin_gap_guardrail|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-07-12", "evidence_available_at_that_date": "infrastructure engineering / reconstruction theme proxy without contract-margin backlog bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["named_contract_or_policy_project_proxy", "backlog_or_fee_visibility_proxy", "margin_bridge_proxy"], "stage3_evidence_fields": ["contract_duration", "cost_pass_through", "gross_margin_conversion", "revision_confirmation"], "stage4b_evidence_fields": ["theme_MFE_without_contract_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_project_loss_or_contract_cancellation_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/054/054930/2024.csv", "profile_path": "atlas/symbol_profiles/054/054930.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-12", "entry_price": 26750, "MFE_30D_pct": 17.57, "MFE_90D_pct": 17.57, "MFE_180D_pct": 17.57, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -24.86, "MAE_90D_pct": -24.86, "MAE_180D_pct": -27.1, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-25", "peak_price": 31450, "drawdown_after_peak_pct": -37.99, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.8, "four_b_full_window_peak_proximity": 0.7, "four_b_timing_verdict": "theme_MFE_should_be_local_4B_watch_or_reject_without_contract_margin_bridge", "four_b_evidence_type": ["theme_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_project_loss_or_contract_break", "trigger_outcome_label": "theme_spike_high_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_4B_too_late", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2003_CA_candidates", "same_entry_group_id": "R1L84-C05-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L84-C05-02", "trigger_id": "R1L84-C05-02-S2FP-20240712", "symbol": "054930", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 40, "customer_quality_score": 15, "policy_or_regulatory_score": 25, "valuation_repricing_score": 30, "execution_risk_score": 70, "cost_pass_through_score": 5, "project_duration_visibility_score": 10, "source_quality_score": 15}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 40, "customer_quality_score": 15, "policy_or_regulatory_score": 25, "valuation_repricing_score": 30, "execution_risk_score": 85, "cost_pass_through_score": 0, "project_duration_visibility_score": 10, "source_quality_score": 5}, "weighted_score_after": 47, "stage_label_after": "Rejected-Stage2 / RiskWatch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "cost_pass_through_score", "source_quality_score", "execution_risk_score"], "component_delta_explanation": "C05 requires named EPC/engineering contract economics, backlog/fee duration, cost pass-through and margin bridge before Stage2-Actionable; reconstruction/theme MFE alone is demoted.", "MFE_90D_pct": 17.57, "MAE_90D_pct": -24.86, "score_return_alignment_label": "theme_spike_high_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_4B_too_late"}
{"row_type": "case", "case_id": "R1L84-C05-03", "symbol": "002150", "company_name": "도화엔지니어링", "round": "R1", "loop": 84, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "ENGINEERING_DESIGN_OVERSEAS_INFRA_CONTRACT_MARGIN_BRIDGE_VS_RECONSTRUCTION_THEME_FADE", "case_type": "engineering_order_theme_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R1L84-C05-03-S2FP-20240712", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "low_quality_MFE_high_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive", "price_source": "Songdaiki/stock-web", "notes": "Civil engineering order buzz should stay RiskWatch unless backlog, fee schedule, cost inflation and margin bridge are documented."}
{"row_type": "trigger", "trigger_id": "R1L84-C05-03-S2FP-20240712", "case_id": "R1L84-C05-03", "symbol": "002150", "company_name": "도화엔지니어링", "round": "R1", "loop": 84, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "ENGINEERING_DESIGN_OVERSEAS_INFRA_CONTRACT_MARGIN_BRIDGE_VS_RECONSTRUCTION_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|EPC_engineering_contract_margin_gap_guardrail|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-07-12", "evidence_available_at_that_date": "civil engineering order/infra theme proxy without backlog-to-margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["named_contract_or_policy_project_proxy", "backlog_or_fee_visibility_proxy", "margin_bridge_proxy"], "stage3_evidence_fields": ["contract_duration", "cost_pass_through", "gross_margin_conversion", "revision_confirmation"], "stage4b_evidence_fields": ["theme_MFE_without_contract_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_project_loss_or_contract_cancellation_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002150/2024.csv", "profile_path": "atlas/symbol_profiles/002/002150.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-12", "entry_price": 7460, "MFE_30D_pct": 10.99, "MFE_90D_pct": 10.99, "MFE_180D_pct": 10.99, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -14.88, "MAE_90D_pct": -14.88, "MAE_180D_pct": -17.56, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-25", "peak_price": 8280, "drawdown_after_peak_pct": -25.72, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "short_theme_MFE_rejected_without_orderbook_margin_bridge", "four_b_evidence_type": ["theme_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_project_loss_or_contract_break", "trigger_outcome_label": "low_quality_MFE_high_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_after_old_2013_CA_candidates", "same_entry_group_id": "R1L84-C05-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L84-C05-03", "trigger_id": "R1L84-C05-03-S2FP-20240712", "symbol": "002150", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 40, "customer_quality_score": 15, "policy_or_regulatory_score": 25, "valuation_repricing_score": 30, "execution_risk_score": 70, "cost_pass_through_score": 5, "project_duration_visibility_score": 10, "source_quality_score": 15}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 40, "customer_quality_score": 15, "policy_or_regulatory_score": 25, "valuation_repricing_score": 30, "execution_risk_score": 85, "cost_pass_through_score": 0, "project_duration_visibility_score": 10, "source_quality_score": 5}, "weighted_score_after": 47, "stage_label_after": "Rejected-Stage2 / RiskWatch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "cost_pass_through_score", "source_quality_score", "execution_risk_score"], "component_delta_explanation": "C05 requires named EPC/engineering contract economics, backlog/fee duration, cost pass-through and margin bridge before Stage2-Actionable; reconstruction/theme MFE alone is demoted.", "MFE_90D_pct": 10.99, "MAE_90D_pct": -14.88, "score_return_alignment_label": "low_quality_MFE_high_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive"}
{"row_type": "case", "case_id": "R1L84-C05-04", "symbol": "023350", "company_name": "한국종합기술", "round": "R1", "loop": 84, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "ENGINEERING_DESIGN_OVERSEAS_INFRA_CONTRACT_MARGIN_BRIDGE_VS_RECONSTRUCTION_THEME_FADE", "case_type": "small_engineering_theme_false_positive_with_delayed_squeeze", "positive_or_counterexample": "counterexample", "best_trigger": "R1L84-C05-04-S2FP-20240712", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "short_MFE_high_MAE_delayed_squeeze_not_stage2", "current_profile_verdict": "current_profile_false_positive_delayed_squeeze", "price_source": "Songdaiki/stock-web", "notes": "A delayed squeeze after a large MAE should not validate the original Stage2 trigger unless contract economics were present at entry."}
{"row_type": "trigger", "trigger_id": "R1L84-C05-04-S2FP-20240712", "case_id": "R1L84-C05-04", "symbol": "023350", "company_name": "한국종합기술", "round": "R1", "loop": 84, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "fine_archetype_id": "ENGINEERING_DESIGN_OVERSEAS_INFRA_CONTRACT_MARGIN_BRIDGE_VS_RECONSTRUCTION_THEME_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|EPC_engineering_contract_margin_gap_guardrail|4B_non_price_requirement_stress_test|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-07-12", "evidence_available_at_that_date": "infra engineering / reconstruction policy theme proxy without confirmed contract economics", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["named_contract_or_policy_project_proxy", "backlog_or_fee_visibility_proxy", "margin_bridge_proxy"], "stage3_evidence_fields": ["contract_duration", "cost_pass_through", "gross_margin_conversion", "revision_confirmation"], "stage4b_evidence_fields": ["theme_MFE_without_contract_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_project_loss_or_contract_cancellation_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/023/023350/2024.csv", "profile_path": "atlas/symbol_profiles/023/023350.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-12", "entry_price": 5390, "MFE_30D_pct": 3.34, "MFE_90D_pct": 3.34, "MFE_180D_pct": 15.77, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -17.99, "MAE_90D_pct": -17.99, "MAE_180D_pct": -17.99, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-04-07", "peak_price": 6240, "drawdown_after_peak_pct": -20.67, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "delayed_microcap_squeeze_not_valid_stage2_without_contract_margin_bridge", "four_b_evidence_type": ["theme_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_project_loss_or_contract_break", "trigger_outcome_label": "short_MFE_high_MAE_delayed_squeeze_not_stage2", "current_profile_verdict": "current_profile_false_positive_delayed_squeeze", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_180D_window_no_profile_CA_candidate", "same_entry_group_id": "R1L84-C05-04", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L84-C05-04", "trigger_id": "R1L84-C05-04-S2FP-20240712", "symbol": "023350", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "raw_component_scores_before": {"contract_score": 10, "backlog_visibility_score": 10, "margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 40, "customer_quality_score": 15, "policy_or_regulatory_score": 25, "valuation_repricing_score": 30, "execution_risk_score": 70, "cost_pass_through_score": 5, "project_duration_visibility_score": 10, "source_quality_score": 15}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"contract_score": 0, "backlog_visibility_score": 0, "margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 40, "customer_quality_score": 15, "policy_or_regulatory_score": 25, "valuation_repricing_score": 30, "execution_risk_score": 85, "cost_pass_through_score": 0, "project_duration_visibility_score": 10, "source_quality_score": 5}, "weighted_score_after": 47, "stage_label_after": "Rejected-Stage2 / RiskWatch", "changed_components": ["contract_score", "backlog_visibility_score", "margin_bridge_score", "cost_pass_through_score", "source_quality_score", "execution_risk_score"], "component_delta_explanation": "C05 requires named EPC/engineering contract economics, backlog/fee duration, cost pass-through and margin bridge before Stage2-Actionable; reconstruction/theme MFE alone is demoted.", "MFE_90D_pct": 3.34, "MAE_90D_pct": -17.99, "score_return_alignment_label": "short_MFE_high_MAE_delayed_squeeze_not_stage2", "current_profile_verdict": "current_profile_false_positive_delayed_squeeze"}
{"row_type": "shadow_weight", "axis": "C05_engineering_EPC_contract_backlog_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Engineering/EPC theme rerating requires named contract economics, backlog/fee duration, cost pass-through and margin bridge; reconstruction/infrastructure theme MFE alone fades into high MAE.", "backtest_effect": "keeps 053690 only with high-MAE/local 4B watch; demotes 054930/002150/023350 false positives", "trigger_ids": "R1L84-C05-01-S2A-20240712|R1L84-C05-02-S2FP-20240712|R1L84-C05-03-S2FP-20240712|R1L84-C05-04-S2FP-20240712", "calibration_usable_count": 4, "new_independent_case_count": 4, "counterexample_count": 3, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R1", "loop": 84, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C05_EPC_MEGA_CONTRACT_MARGIN_GAP", "new_independent_case_count": 4, "reused_case_count": 0, "new_symbol_count": 4, "new_trigger_family_count": 4, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail"], "residual_error_types_found": ["engineering_contract_theme_false_positive_high_MAE", "EPC_margin_bridge_required", "source_proxy_runtime_promotion_risk", "local_4B_needed_after_contract_theme_MFE", "delayed_squeeze_not_original_stage2_validation"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C05, test a canonical-archetype guard requiring named EPC/engineering contract economics, backlog/fee duration, cost pass-through and margin bridge before Stage2-Actionable.

## 27. Next Round State

```text
completed_round = R1
completed_loop = 84
next_round = R2
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
