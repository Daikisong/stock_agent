# E2R Stock-Web v12 Residual Research — R10 Loop 85 / L9 / C30

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R10",
  "scheduled_loop": 85,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R10",
  "completed_loop": 85,
  "computed_next_round": "R11",
  "computed_next_loop": 85,
  "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING",
  "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK",
  "fine_archetype_id": "SMALL_MID_BUILDER_PF_THEME_ORDERBOOK_MARGIN_BRIDGE_VS_HOUSING_SQUEEZE_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "construction_PF_balance_sheet_guardrail",
    "small_mid_builder_orderbook_cashflow_margin_bridge_test",
    "housing_theme_squeeze_vs_PF_refinancing_bridge_split",
    "local_4B_timing_after_construction_MFE",
    "hard_4C_non_price_debt_project_loss_protection",
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
scheduled_loop = 85
allowed_large_sector = L9_CONSTRUCTION_REALESTATE_HOUSING
selected_large_sector = L9_CONSTRUCTION_REALESTATE_HOUSING
selected_canonical_archetype_id = C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK
computed_next_round = R11
computed_next_loop = 85
round_schedule_status = valid
round_sector_consistency = pass
```

R10 is the construction / real estate / housing round. Loop84 already tested mid-builder recovery with `013580`, `004960`, and `013360`; loop85 therefore shifts to under-used small/mid builder rows.

The tested mechanism:

```text
housing / small-builder / PF recovery headline
→ PF refinancing and debt maturity control
→ orderbook quality and cash-flow bridge
→ project-loss path and project-margin bridge
→ durable rerating or local 4B / low-MFE theme fade
```

C30 is the structural-load test. A housing headline can lift the roof, but PF, debt, cash flow and project margin hold the building.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C30 top-covered symbols include `047040`, `006360`, `UNKNOWN_SYMBOL`, `294870`, `005960`, and `000720`. This run avoids that top-covered set and also avoids loop84 R10 symbols:

```text
previous_loop84_R10_symbols = 013580 / 004960 / 013360
selected_loop85_symbols = 001260 / 017000 / 002780
```

All three are treated as new independent C30 small/mid-builder PF / orderbook / margin-bridge cases for this loop. No hard duplicate is intentionally reused.

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
| 001260 | 남광토건 | `atlas/symbol_profiles/001/001260.json` | old CA candidates through 2016; selected 2024/2025 forward window clean |
| 017000 | 신원종합개발 | `atlas/symbol_profiles/017/017000.json` | old CA candidates through 2015; selected 2024/2025 forward window clean |
| 002780 | 진흥기업 | `atlas/symbol_profiles/002/002780.json` | old CA candidates through 2015; selected 2024/2025 forward window clean |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R10L85-C30-01 | 001260 | 2024-07-12 | 6,090 | 180D | clean | true |
| R10L85-C30-02 | 017000 | 2024-07-12 | 2,465 | 180D | clean | true |
| R10L85-C30-03 | 002780 | 2024-07-12 | 930 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | SMALL_MID_BUILDER_ORDERBOOK_PF_RECOVERY | keep Stage2 only with PF, debt maturity, orderbook quality, cash-flow and project-margin bridge |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | SMALL_BUILDER_HOUSING_THEME_MFE_RISKWATCH | allow Stage2 only with local 4B/high-MAE watch until project cash-flow and margin are repaired |
| C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | LOW_PBR_CONSTRUCTION_THEME_FADE | reject low-MFE construction/value-up beta without refinancing, liquidity and orderbook margin bridge |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R10L85-C30-01 | 001260 | 남광토건 | Stage2-Actionable | 2024-07-12 | 6,090 | 43.84 | -2.3 | current_profile_partially_correct_local_4B_watch_needed |
| R10L85-C30-02 | 017000 | 신원종합개발 | Stage2-Actionable | 2024-07-12 | 2,465 | 73.63 | -8.52 | current_profile_4B_too_late_after_housing_theme_MFE |
| R10L85-C30-03 | 002780 | 진흥기업 | Stage2-FalsePositive | 2024-07-12 | 930 | 5.05 | -25.7 | current_profile_false_positive_low_MFE_high_MAE |

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

This MD therefore creates a source-repair queue and a C30 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: PF refinancing, debt maturity schedule, project-loss provisioning, cash-flow bridge, orderbook quality, project-margin bridge, company disclosure, filing or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 001260 | `atlas/ohlcv_tradable_by_symbol_year/001/001260/2024.csv` and `2025.csv` | `atlas/symbol_profiles/001/001260.json` |
| 017000 | `atlas/ohlcv_tradable_by_symbol_year/017/017000/2024.csv` and `2025.csv` | `atlas/symbol_profiles/017/017000.json` |
| 002780 | `atlas/ohlcv_tradable_by_symbol_year/002/002780/2024.csv` and `2025.csv` | `atlas/symbol_profiles/002/002780.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 001260 / 남광토건

C30 small/mid builder recovery positive. The price path produced strong MFE with very controlled MAE, but the label still needs PF, orderbook and cash-flow repair before clean Green.

### Case 2 — 017000 / 신원종합개발

C30 small-builder housing-theme MFE positive with local 4B watch. The MFE was very strong, but the later drawdown shows that full 4B timing can be late if the model waits for a full-window signal. It should remain local 4B / project-margin watch until source repair.

### Case 3 — 002780 / 진흥기업

C30 low-MFE construction/PF theme false positive. The entry path created only small MFE and then bled lower. This rejects low-PBR construction beta without PF refinancing, liquidity and margin evidence.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 001260 | 6,090 | 40.39 | -0.66 | 40.39 | -2.30 | 43.84 | -2.30 | 2025-02-06 / 8,760 | -17.24 |
| 017000 | 2,465 | 73.63 | -8.52 | 73.63 | -8.52 | 73.63 | -8.52 | 2024-08-20 / 4,280 | -41.00 |
| 002780 | 930 | 5.05 | -14.30 | 5.05 | -14.30 | 5.05 | -25.70 | 2024-07-12 / 977 | -29.27 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R10L85-C30-01 | Stage2-Actionable if PF/orderbook bridge exists | high MFE, low MAE | partially correct; source repair needed |
| R10L85-C30-02 | Stage2-Actionable if housing theme is over-credited | very high MFE, later drawdown | local 4B too late unless watch added |
| R10L85-C30-03 | risk of treating low-PBR construction theme as Stage2 | low MFE / high MAE | false positive |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C30, the residual is whether construction/PF MFE becomes clean Stage2/Green before refinancing, debt/liquidity, cash-flow and project-margin bridge are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R10L85-C30-01 | 0.82 | 0.72 | local 4B watch after builder recovery MFE if PF/orderbook/margin bridge stalls |
| R10L85-C30-02 | 0.82 | 0.72 | local 4B watch required when small-builder MFE outruns project cash-flow bridge |
| R10L85-C30-03 | 0.35 | 0.30 | construction value-up/PF theme rejected without liquidity/orderbook margin bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_debt_project_loss_or_margin_break
hard_4c_price_only_allowed = false
```

Price drawdown alone is not hard 4C. C30 hard 4C requires confirmed PF refinancing failure, debt/liquidity break, project-loss provisioning, impairment, or project-margin thesis break.

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
candidate_axis = C30_small_mid_builder_PF_debt_orderbook_cashflow_margin_bridge_required
effect = keep small/mid-builder positives with local 4B/high-MAE watch; demote low-MFE construction-theme false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 39.69 | -8.37 | may over-credit small-builder/housing theme MFE | needs C30 source repair |
| P1 canonical shadow bridge profile | 3 | 57.01 on kept positives | -5.41 on kept positives | demotes 002780 | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R10L85-C30-01 | 76 | Stage2-Actionable | 74 | Stage2-Actionable + local 4B/PF-margin watch | partially aligned |
| R10L85-C30-02 | 76 | Stage2-Actionable | 70 | Stage2-Actionable + local 4B/PF-margin watch | partially aligned |
| R10L85-C30-03 | 58 | Stage2-Watch/FalsePositive | 44 | Rejected-Stage2 / Construction-PF theme RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L9_CONSTRUCTION_REALESTATE_HOUSING | C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK | SMALL_MID_BUILDER_PF_THEME_ORDERBOOK_MARGIN_BRIDGE_VS_HOUSING_SQUEEZE_FADE | 2 | 1 | 3-watch | 0-hard | 3 | 0 | 3 | 2 | no | yes | source repair needed |

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
  - small_mid_builder_theme_false_positive_low_MFE_high_MAE
  - PF_debt_orderbook_cashflow_margin_bridge_required
  - local_4B_late_after_housing_theme_MFE
  - source_proxy_runtime_promotion_risk
  - hard_4C_requires_non_price_debt_project_loss_break
new_axis_proposed: false
existing_axis_strengthened:
  - C30_small_mid_builder_PF_debt_orderbook_cashflow_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - hard_4C_requires_non_price_thesis_break
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C30_small_mid_builder_PF_debt_orderbook_cashflow_margin_bridge_required
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
- project-loss provisioning path
- orderbook quality and cash-flow bridge
- project-margin conversion
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C30_small_mid_builder_PF_debt_orderbook_cashflow_margin_bridge_required,canonical_archetype_specific,L9_CONSTRUCTION_REALESTATE_HOUSING,C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK,0,1,+1,"Require PF refinancing, debt/liquidity control, orderbook quality, cash-flow and project-margin bridge before clean Stage2/Green","keeps 001260/017000 with local 4B or high-MAE RiskWatch; demotes 002780","R10L85-C30-01-S2A-20240712|R10L85-C30-02-S2A-20240712|R10L85-C30-03-S2FP-20240712",3,3,1,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R10L85-C30-01", "symbol": "001260", "company_name": "남광토건", "round": "R10", "loop": 85, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_MID_BUILDER_PF_THEME_ORDERBOOK_MARGIN_BRIDGE_VS_HOUSING_SQUEEZE_FADE", "case_type": "mid_small_builder_orderbook_PF_recovery_positive_with_local_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R10L85-C30-01-S2A-20240712", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "strong_positive_MFE_but_PF_orderbook_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C30 can keep small/mid-builder Stage2 only when PF exposure, debt maturity, orderbook quality, cash-flow and project-margin bridge are visible."}
{"row_type": "trigger", "trigger_id": "R10L85-C30-01-S2A-20240712", "case_id": "R10L85-C30-01", "symbol": "001260", "company_name": "남광토건", "round": "R10", "loop": 85, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_MID_BUILDER_PF_THEME_ORDERBOOK_MARGIN_BRIDGE_VS_HOUSING_SQUEEZE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|construction_PF_balance_sheet_guardrail|small_mid_builder_theme_vs_PF_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-12", "evidence_available_at_that_date": "small/mid builder orderbook, housing-policy/PF recovery and balance-sheet normalization proxy; primary PF, debt maturity and project-margin evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["PF_refinancing_proxy", "orderbook_quality_proxy", "debt_liquidity_proxy", "project_margin_proxy"], "stage3_evidence_fields": ["confirmed_refinancing", "cash_flow_bridge", "loss_provision_path", "orderbook_margin_quality", "balance_sheet_trust"], "stage4b_evidence_fields": ["construction_MFE_without_PF_bridge", "housing_theme_squeeze", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_debt_liquidity_or_project_loss_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/001/001260/2024.csv", "profile_path": "atlas/symbol_profiles/001/001260.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-12", "entry_price": 6090, "MFE_30D_pct": 40.39, "MFE_90D_pct": 40.39, "MFE_180D_pct": 43.84, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -0.66, "MAE_90D_pct": -2.3, "MAE_180D_pct": -2.3, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-02-06", "peak_price": 8760, "drawdown_after_peak_pct": -17.24, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.82, "four_b_full_window_peak_proximity": 0.72, "four_b_timing_verdict": "local_4B_watch_after_builder_recovery_MFE_if_PF_orderbook_margin_bridge_stalls", "four_b_evidence_type": ["housing_or_construction_MFE_without_PF_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_debt_project_loss_or_margin_break", "trigger_outcome_label": "strong_positive_MFE_but_PF_orderbook_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_2025_window_after_old_2016_CA_candidate", "same_entry_group_id": "R10L85-C30-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L85-C30-01", "trigger_id": "R10L85-C30-01-S2A-20240712", "symbol": "001260", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"PF_refinancing_visibility_score": 35, "debt_liquidity_control_score": 35, "orderbook_quality_score": 45, "project_margin_bridge_score": 35, "cash_flow_bridge_score": 30, "balance_sheet_trust_score": 40, "loss_provision_risk_score": 45, "revision_score": 35, "relative_strength_score": 55, "valuation_repricing_score": 50, "execution_risk_score": 55, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"PF_refinancing_visibility_score": 35, "debt_liquidity_control_score": 35, "orderbook_quality_score": 45, "project_margin_bridge_score": 35, "cash_flow_bridge_score": 30, "balance_sheet_trust_score": 40, "loss_provision_risk_score": 45, "revision_score": 35, "relative_strength_score": 55, "valuation_repricing_score": 50, "execution_risk_score": 55, "source_quality_score": 10, "4B_watch_score": 80}, "weighted_score_after": 74, "stage_label_after": "Stage2-Actionable + local 4B/PF-margin watch", "changed_components": ["PF_refinancing_visibility_score", "debt_liquidity_control_score", "project_margin_bridge_score", "cash_flow_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C30 requires PF refinancing, debt/liquidity control, orderbook quality, cash-flow and project-margin bridge before clean Stage2/Green; housing or low-PBR construction theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 40.39, "MAE_90D_pct": -2.3, "score_return_alignment_label": "strong_positive_MFE_but_PF_orderbook_margin_bridge_required", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed"}
{"row_type": "case", "case_id": "R10L85-C30-02", "symbol": "017000", "company_name": "신원종합개발", "round": "R10", "loop": 85, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_MID_BUILDER_PF_THEME_ORDERBOOK_MARGIN_BRIDGE_VS_HOUSING_SQUEEZE_FADE", "case_type": "small_builder_housing_theme_MFE_positive_but_high_MAE_watch", "positive_or_counterexample": "positive", "best_trigger": "R10L85-C30-02-S2A-20240712", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "very_high_MFE_but_local_4B_and_project_margin_watch_required", "current_profile_verdict": "current_profile_4B_too_late_after_housing_theme_MFE", "price_source": "Songdaiki/stock-web", "notes": "Small-builder theme MFE can be tradable, but clean Green requires PF refinancing, orderbook quality, cash collection and project-margin repair."}
{"row_type": "trigger", "trigger_id": "R10L85-C30-02-S2A-20240712", "case_id": "R10L85-C30-02", "symbol": "017000", "company_name": "신원종합개발", "round": "R10", "loop": 85, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_MID_BUILDER_PF_THEME_ORDERBOOK_MARGIN_BRIDGE_VS_HOUSING_SQUEEZE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|construction_PF_balance_sheet_guardrail|small_mid_builder_theme_vs_PF_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-12", "evidence_available_at_that_date": "small builder housing-policy, redevelopment/orderbook and PF-risk normalization proxy; primary backlog, PF and margin evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["PF_refinancing_proxy", "orderbook_quality_proxy", "debt_liquidity_proxy", "project_margin_proxy"], "stage3_evidence_fields": ["confirmed_refinancing", "cash_flow_bridge", "loss_provision_path", "orderbook_margin_quality", "balance_sheet_trust"], "stage4b_evidence_fields": ["construction_MFE_without_PF_bridge", "housing_theme_squeeze", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_debt_liquidity_or_project_loss_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/017/017000/2024.csv", "profile_path": "atlas/symbol_profiles/017/017000.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-12", "entry_price": 2465, "MFE_30D_pct": 73.63, "MFE_90D_pct": 73.63, "MFE_180D_pct": 73.63, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -8.52, "MAE_90D_pct": -8.52, "MAE_180D_pct": -8.52, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-08-20", "peak_price": 4280, "drawdown_after_peak_pct": -41.0, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.82, "four_b_full_window_peak_proximity": 0.72, "four_b_timing_verdict": "local_4B_watch_required_when_small_builder_MFE_outruns_project_cashflow_margin_bridge", "four_b_evidence_type": ["housing_or_construction_MFE_without_PF_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_debt_project_loss_or_margin_break", "trigger_outcome_label": "very_high_MFE_but_local_4B_and_project_margin_watch_required", "current_profile_verdict": "current_profile_4B_too_late_after_housing_theme_MFE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_2025_window_after_old_2015_CA_candidate", "same_entry_group_id": "R10L85-C30-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L85-C30-02", "trigger_id": "R10L85-C30-02-S2A-20240712", "symbol": "017000", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"PF_refinancing_visibility_score": 35, "debt_liquidity_control_score": 35, "orderbook_quality_score": 45, "project_margin_bridge_score": 35, "cash_flow_bridge_score": 30, "balance_sheet_trust_score": 40, "loss_provision_risk_score": 45, "revision_score": 35, "relative_strength_score": 65, "valuation_repricing_score": 50, "execution_risk_score": 65, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 76, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"PF_refinancing_visibility_score": 35, "debt_liquidity_control_score": 35, "orderbook_quality_score": 45, "project_margin_bridge_score": 35, "cash_flow_bridge_score": 30, "balance_sheet_trust_score": 40, "loss_provision_risk_score": 45, "revision_score": 35, "relative_strength_score": 65, "valuation_repricing_score": 50, "execution_risk_score": 75, "source_quality_score": 10, "4B_watch_score": 80}, "weighted_score_after": 70, "stage_label_after": "Stage2-Actionable + local 4B/PF-margin watch", "changed_components": ["PF_refinancing_visibility_score", "debt_liquidity_control_score", "project_margin_bridge_score", "cash_flow_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C30 requires PF refinancing, debt/liquidity control, orderbook quality, cash-flow and project-margin bridge before clean Stage2/Green; housing or low-PBR construction theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 73.63, "MAE_90D_pct": -8.52, "score_return_alignment_label": "very_high_MFE_but_local_4B_and_project_margin_watch_required", "current_profile_verdict": "current_profile_4B_too_late_after_housing_theme_MFE"}
{"row_type": "case", "case_id": "R10L85-C30-03", "symbol": "002780", "company_name": "진흥기업", "round": "R10", "loop": 85, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_MID_BUILDER_PF_THEME_ORDERBOOK_MARGIN_BRIDGE_VS_HOUSING_SQUEEZE_FADE", "case_type": "construction_valueup_PF_theme_low_MFE_high_MAE_false_positive", "positive_or_counterexample": "counterexample", "best_trigger": "R10L85-C30-03-S2FP-20240712", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "low_MFE_high_MAE_construction_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_high_MAE", "price_source": "Songdaiki/stock-web", "notes": "Low-PBR construction/PF theme should be rejected unless refinancing, debt liquidity, orderbook margin and cash-flow bridge are explicit at entry."}
{"row_type": "trigger", "trigger_id": "R10L85-C30-03-S2FP-20240712", "case_id": "R10L85-C30-03", "symbol": "002780", "company_name": "진흥기업", "round": "R10", "loop": 85, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "fine_archetype_id": "SMALL_MID_BUILDER_PF_THEME_ORDERBOOK_MARGIN_BRIDGE_VS_HOUSING_SQUEEZE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|construction_PF_balance_sheet_guardrail|small_mid_builder_theme_vs_PF_margin_bridge|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-07-12", "evidence_available_at_that_date": "construction/PF recovery and low-PBR/value-up theme proxy without clear refinancing, orderbook quality, liquidity or margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["PF_refinancing_proxy", "orderbook_quality_proxy", "debt_liquidity_proxy", "project_margin_proxy"], "stage3_evidence_fields": ["confirmed_refinancing", "cash_flow_bridge", "loss_provision_path", "orderbook_margin_quality", "balance_sheet_trust"], "stage4b_evidence_fields": ["construction_MFE_without_PF_bridge", "housing_theme_squeeze", "post_peak_drawdown"], "stage4c_evidence_fields": ["hard_debt_liquidity_or_project_loss_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/002/002780/2024.csv", "profile_path": "atlas/symbol_profiles/002/002780.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-12", "entry_price": 930, "MFE_30D_pct": 5.05, "MFE_90D_pct": 5.05, "MFE_180D_pct": 5.05, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -14.3, "MAE_90D_pct": -14.3, "MAE_180D_pct": -25.7, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-12", "peak_price": 977, "drawdown_after_peak_pct": -29.27, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "construction_valueup_theme_rejected_without_PF_orderbook_liquidity_margin_bridge", "four_b_evidence_type": ["housing_or_construction_MFE_without_PF_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_debt_project_loss_or_margin_break", "trigger_outcome_label": "low_MFE_high_MAE_construction_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_high_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_2025_window_after_old_2015_CA_candidates", "same_entry_group_id": "R10L85-C30-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R10L85-C30-03", "trigger_id": "R10L85-C30-03-S2FP-20240712", "symbol": "002780", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "raw_component_scores_before": {"PF_refinancing_visibility_score": 5, "debt_liquidity_control_score": 10, "orderbook_quality_score": 10, "project_margin_bridge_score": 5, "cash_flow_bridge_score": 5, "balance_sheet_trust_score": 15, "loss_provision_risk_score": 75, "revision_score": 15, "relative_strength_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 80, "source_quality_score": 15, "4B_watch_score": 75}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"PF_refinancing_visibility_score": 0, "debt_liquidity_control_score": 0, "orderbook_quality_score": 10, "project_margin_bridge_score": 0, "cash_flow_bridge_score": 0, "balance_sheet_trust_score": 15, "loss_provision_risk_score": 75, "revision_score": 15, "relative_strength_score": 25, "valuation_repricing_score": 25, "execution_risk_score": 90, "source_quality_score": 5, "4B_watch_score": 85}, "weighted_score_after": 44, "stage_label_after": "Rejected-Stage2 / Construction-PF theme RiskWatch", "changed_components": ["PF_refinancing_visibility_score", "debt_liquidity_control_score", "project_margin_bridge_score", "cash_flow_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C30 requires PF refinancing, debt/liquidity control, orderbook quality, cash-flow and project-margin bridge before clean Stage2/Green; housing or low-PBR construction theme MFE alone is demoted or wrapped with local 4B/high-MAE watch.", "MFE_90D_pct": 5.05, "MAE_90D_pct": -14.3, "score_return_alignment_label": "low_MFE_high_MAE_construction_theme_false_positive", "current_profile_verdict": "current_profile_false_positive_low_MFE_high_MAE"}
{"row_type": "shadow_weight", "axis": "C30_small_mid_builder_PF_debt_orderbook_cashflow_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Construction/PF rerating requires PF refinancing, debt/liquidity control, orderbook quality, cash-flow and project-margin bridge; housing theme or low-PBR construction beta without bridge should not become clean Stage2/Green.", "backtest_effect": "keeps 001260/017000 with local 4B or high-MAE RiskWatch; demotes 002780 low-MFE construction-theme false positive", "trigger_ids": "R10L85-C30-01-S2A-20240712|R10L85-C30-02-S2A-20240712|R10L85-C30-03-S2FP-20240712", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 1, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R10", "loop": 85, "large_sector_id": "L9_CONSTRUCTION_REALESTATE_HOUSING", "canonical_archetype_id": "C30_CONSTRUCTION_PF_BALANCE_SHEET_BREAK", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["small_mid_builder_theme_false_positive_low_MFE_high_MAE", "PF_debt_orderbook_cashflow_margin_bridge_required", "local_4B_late_after_housing_theme_MFE", "source_proxy_runtime_promotion_risk", "hard_4C_requires_non_price_debt_project_loss_break"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
completed_loop = 85
next_round = R11
next_loop = 85
round_schedule_status = valid
round_sector_consistency = pass
```

## 28. Source Notes

```text
MAIN_EXECUTION_PROMPT = docs/core/e2r_v12_prompt_round_scheduler_corrected.txt
NO_REPEAT_INDEX = docs/core/V12_Research_No_Repeat_Index.md
price_source = Songdaiki/stock-web
```
