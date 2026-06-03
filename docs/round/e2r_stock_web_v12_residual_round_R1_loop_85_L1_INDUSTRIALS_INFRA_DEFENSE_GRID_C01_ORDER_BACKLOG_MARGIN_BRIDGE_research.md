# E2R Stock-Web v12 Residual Research — R1 Loop 85 / L1 / C01

## 0. Research Metadata

```json
{
  "research_session": "post_calibrated_sector_archetype_residual_research",
  "mode": "historical_trigger_level_calibration_after_stock_web_ohlc_breakthrough_v12",
  "scheduled_round": "R1",
  "scheduled_loop": 85,
  "round_schedule_status": "valid",
  "round_sector_consistency": "pass",
  "completed_round": "R1",
  "completed_loop": 85,
  "computed_next_round": "R2",
  "computed_next_loop": 85,
  "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID",
  "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE",
  "fine_archetype_id": "INDUSTRIAL_FITTINGS_OFFSHORE_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_ORDER_THEME_HIGH_MAE_FADE",
  "loop_objective": [
    "coverage_gap_fill",
    "counterexample_mining",
    "order_backlog_margin_bridge_guardrail",
    "industrial_fittings_backlog_delivery_margin_bridge_test",
    "offshore_order_theme_high_MAE_counterexample_test",
    "local_4B_timing_after_order_MFE",
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
scheduled_round = R1
scheduled_loop = 85
allowed_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_large_sector = L1_INDUSTRIALS_INFRA_DEFENSE_GRID
selected_canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE
computed_next_round = R2
computed_next_loop = 85
round_schedule_status = valid
round_sector_consistency = pass
```

R1 starts loop85 after loop84 R13 completed. This run selects C01 because C01 remains a thinner industrials axis than C02/C03/C04, and loop84 already used C05.

The tested mechanism:

```text
industrial order / backlog / EPC project headline
→ backlog quality and customer/project durability
→ delivery schedule and utilization
→ ASP or cost pass-through
→ gross / OP margin conversion
→ durable rerating or local 4B / high-MAE fade
```

C01 is the difference between an order book printed on paper and an order book converted into margin. The bridge is delivery, not just announcement.

## 3. Previous Coverage / Duplicate Avoidance Check

No-Repeat is used only as a duplicate ledger.

```text
hard_duplicate_key = canonical_archetype_id + symbol + trigger_type + entry_date
```

C01 top-covered symbols include `010620`, `329180`, `009540`, `010140`, `077970`, and `082740`. This run avoids that top-covered set and uses:

```text
014620 / 성광벤드
023160 / 태광
100090 / SK오션플랜트
```

All three are treated as new independent C01 order-backlog / margin-bridge cases for this loop. No hard duplicate is intentionally reused.

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
| 014620 | 성광벤드 | `atlas/symbol_profiles/014/014620.json` | no profile-level CA candidate |
| 023160 | 태광 | `atlas/symbol_profiles/023/023160.json` | old CA candidates only; selected 2024 window clean |
| 100090 | SK오션플랜트 | `atlas/symbol_profiles/100/100090.json` | old 2022 CA candidate; selected 2024 window clean |

## 5. Historical Eligibility Gate

| case_id | symbol | entry_date | entry_price | forward window | 180D status | calibration_usable |
|---|---:|---|---:|---:|---|---|
| R1L85-C01-01 | 014620 | 2024-07-12 | 11,540 | 180D | clean | true |
| R1L85-C01-02 | 023160 | 2024-07-12 | 13,410 | 180D | clean | true |
| R1L85-C01-03 | 100090 | 2024-07-12 | 14,020 | 180D | clean | true |

## 6. Canonical Archetype Compression Map

| canonical_archetype_id | fine/deep route | keep / reject logic |
|---|---|---|
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | INDUSTRIAL_FITTINGS_BACKLOG_DELIVERY_MARGIN | keep Stage2 only with backlog quality, delivery schedule, ASP/cost pass-through and margin bridge |
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | OFFSHORE_PROJECT_ORDER_THEME_HIGH_MAE | reject or RiskWatch when order theme lacks utilization/project-margin bridge |
| C01_ORDER_BACKLOG_MARGIN_BRIDGE | ORDER_MFE_LOCAL_4B_WATCH | local 4B when MFE outruns delivery/margin confirmation |

## 7. Case Selection Summary

| case_id | symbol | company | trigger_type | entry_date | entry_price | MFE_180D_pct | MAE_180D_pct | current_profile_verdict |
|---|---:|---|---|---|---:|---:|---:|---|
| R1L85-C01-01 | 014620 | 성광벤드 | Stage2-Actionable | 2024-07-12 | 11,540 | 181.63 | -1.13 | current_profile_partially_correct_local_4B_watch_needed |
| R1L85-C01-02 | 023160 | 태광 | Stage2-Actionable | 2024-07-12 | 13,410 | 33.63 | -4.55 | current_profile_partially_correct_local_4B_watch_needed |
| R1L85-C01-03 | 100090 | SK오션플랜트 | Stage2-FalsePositive | 2024-07-12 | 14,020 | 15.55 | -26.53 | current_profile_false_positive_high_MAE |

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

This MD therefore creates a source-repair queue and a C01 shadow guardrail candidate. It must not be promoted directly into runtime weights until a later source-repair pass attaches primary evidence URLs: order disclosure, backlog, delivery schedule, customer quality, project utilization, ASP/cost pass-through, gross/OP margin bridge, company disclosure or report evidence.

## 10. Price Data Source Map

| symbol | shard path | profile path |
|---|---|---|
| 014620 | `atlas/ohlcv_tradable_by_symbol_year/014/014620/2024.csv` and `2025.csv` | `atlas/symbol_profiles/014/014620.json` |
| 023160 | `atlas/ohlcv_tradable_by_symbol_year/023/023160/2024.csv` | `atlas/symbol_profiles/023/023160.json` |
| 100090 | `atlas/ohlcv_tradable_by_symbol_year/100/100090/2024.csv` | `atlas/symbol_profiles/100/100090.json` |

## 11. Case-by-Case Trigger Grid

### Case 1 — 014620 / 성광벤드

C01 industrial fittings positive with local 4B watch. The entry path generated very large forward MFE and the profile is clean from corporate-action contamination. The model should keep the positive but not turn it into clean Green unless backlog quality, delivery schedule and margin bridge are source-repaired.

### Case 2 — 023160 / 태광

C01 order-cycle positive with post-peak watch. The price path delivered strong MFE after the July entry, but the peak came quickly. This is useful as a local-4B lesson: order MFE can outrun delivery/margin confirmation.

### Case 3 — 100090 / SK오션플랜트

C01 offshore/order-theme counterexample. The entry path had a modest later MFE, but the early MAE was too deep. Offshore/orderbook theme evidence should be rejected unless project execution, utilization and margin bridge are explicit.

## 12. Trigger-Level OHLC Backtest Tables

| symbol | entry | MFE30 | MAE30 | MFE90 | MAE90 | MFE180 | MAE180 | peak | post-peak DD |
|---|---:|---:|---:|---:|---:|---:|---:|---|---:|
| 014620 | 11,540 | 46.45 | -1.13 | 46.45 | -1.13 | 181.63 | -1.13 | 2025-01-17 / 32,500 | -30.62 |
| 023160 | 13,410 | 33.63 | -3.43 | 33.63 | -4.55 | 33.63 | -4.55 | 2024-07-26 / 17,920 | -28.57 |
| 100090 | 14,020 | 10.99 | -26.53 | 15.55 | -26.53 | 15.55 | -26.53 | 2024-09-24 / 16,200 | -10.31 |

## 13. Current Calibrated Profile Stress Test

| case_id | P0 likely behavior | actual path | verdict |
|---|---|---|---|
| R1L85-C01-01 | Stage2-Actionable if backlog/margin bridge exists | extreme MFE, later drawdown | partially correct; local 4B watch needed |
| R1L85-C01-02 | Stage2-Actionable if delivery/margin bridge exists | strong MFE, post-peak fade | partially correct; local 4B watch needed |
| R1L85-C01-03 | risk of treating offshore order theme as Stage2 | modest MFE / high MAE | false positive / high-MAE guardrail |

## 14. Stage2 / Yellow / Green Comparison

```text
green_lateness_ratio = not_applicable
reason = no confirmed Stage3-Green trigger is assigned in this residual MD
```

For C01, the residual is not Green lateness. The residual is whether order/backlog MFE becomes clean Stage2/Green before delivery schedule, utilization and margin conversion are proven.

## 15. 4B Local vs Full-window Timing Audit

| case_id | local proximity | full-window proximity | verdict |
|---|---:|---:|---|
| R1L85-C01-01 | 0.85 | 0.75 | local 4B watch after order/backlog MFE if delivery margin bridge stalls |
| R1L85-C01-02 | 0.85 | 0.75 | local 4B watch when fittings order MFE outruns backlog margin confirmation |
| R1L85-C01-03 | 0.35 | 0.30 | order theme rejected without backlog delivery utilization margin bridge |

## 16. 4C Protection Audit

No hard 4C is promoted from this file.

```text
four_c_protection_label = hard_4C_requires_non_price_order_cancel_or_margin_break
hard_4c_price_only_allowed = false
```

## 17. Sector-Specific Rule Candidate

```text
rule_scope = no_new_global_rule
sector_specific_rule_candidate = L1 industrial order/backlog rows need backlog quality, delivery schedule, utilization, ASP/cost pass-through and gross/OP margin conversion before clean Stage2/Green
confidence = low
reason = all evidence rows are source_proxy_only / evidence_url_pending
```

## 18. Canonical-Archetype Rule Candidate

```text
canonical_archetype_id = C01_ORDER_BACKLOG_MARGIN_BRIDGE
candidate_axis = C01_order_backlog_delivery_margin_bridge_required
effect = keep order-cycle positives with local 4B/margin bridge watch; demote offshore order-theme high-MAE false positives
production_scoring_changed = false
shadow_weight_only = true
do_not_propose_new_weight_delta = true
```

## 19. Before / After Backtest Comparison

| profile | eligible triggers | avg MFE90 | avg MAE90 | false-positive behavior | verdict |
|---|---:|---:|---:|---|---|
| P0 e2r_2_1_stock_web_calibrated_proxy | 3 | 31.88 | -10.74 | may over-credit order/backlog theme without delivery-margin bridge | needs C01 bridge repair |
| P1 canonical shadow bridge profile | 3 | 40.04 on kept positives | -2.84 on kept positives | demotes 100090 | better alignment, source repair required |

## 20. Score-Return Alignment Matrix

| case_id | weighted before | label before | weighted after | label after | alignment |
|---|---:|---|---:|---|---|
| R1L85-C01-01 | 80 | Stage2-Actionable | 77 | Stage2-Actionable + local 4B/margin bridge watch | partially aligned |
| R1L85-C01-02 | 80 | Stage2-Actionable | 77 | Stage2-Actionable + local 4B/margin bridge watch | partially aligned |
| R1L85-C01-03 | 58 | Stage2-Watch/FalsePositive | 45 | Rejected-Stage2 / Order-theme RiskWatch | improved |

## 21. Coverage Matrix

| large_sector_id | canonical_archetype_id | fine_archetype_id | positive | counterexample | 4B | 4C | new cases | reused | usable triggers | current errors | sector rule | canonical rule | coverage gap after |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---|---|---|
| L1_INDUSTRIALS_INFRA_DEFENSE_GRID | C01_ORDER_BACKLOG_MARGIN_BRIDGE | INDUSTRIAL_FITTINGS_OFFSHORE_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_ORDER_THEME_HIGH_MAE_FADE | 2 | 1 | 3-watch | 0 | 3 | 0 | 3 | 2 | no | yes | source repair needed |

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
  - industrial_order_theme_false_positive_high_MAE
  - order_backlog_delivery_margin_bridge_required
  - local_4B_late_after_order_MFE
  - source_proxy_runtime_promotion_risk
  - high_MAE_positive_Green_blocker
new_axis_proposed: false
existing_axis_strengthened:
  - C01_order_backlog_delivery_margin_bridge_required
  - source_proxy_only_blocks_runtime_promotion
  - local_4B_watch_before_full_4B_when_MFE_outruns_bridge
  - high_MAE_blocks_clean_Green
existing_axis_weakened: null
existing_axis_kept:
  - full_4b_requires_non_price_evidence
  - hard_4c_thesis_break_routes_to_4c
sector_specific_rule_candidate: null
canonical_archetype_rule_candidate: C01_order_backlog_delivery_margin_bridge_required
no_new_signal_reason: null
loop_contribution_label: canonical_archetype_rule_candidate
do_not_propose_new_weight_delta: true
```

This loop adds 3 new independent cases, 1 counterexample, and 2 residual errors for R1/L1_INDUSTRIALS_INFRA_DEFENSE_GRID/C01_ORDER_BACKLOG_MARGIN_BRIDGE.

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
- order disclosure and backlog quality
- delivery schedule and utilization
- ASP/cost pass-through
- gross/OP margin conversion
- production scoring implementation
```

## 24. Shadow Weight Calibration

```csv
row_type,axis,scope,large_sector_id,canonical_archetype_id,baseline_value,tested_value,delta,reason,backtest_effect,trigger_ids,calibration_usable_count,new_independent_case_count,counterexample_count,confidence,proposal_type,notes
shadow_weight,C01_order_backlog_delivery_margin_bridge_required,canonical_archetype_specific,L1_INDUSTRIALS_INFRA_DEFENSE_GRID,C01_ORDER_BACKLOG_MARGIN_BRIDGE,0,1,+1,"Require backlog quality, delivery schedule, utilization, ASP/cost pass-through and margin conversion before clean Stage2/Green","keeps 014620/023160 with local 4B or margin-bridge watch; demotes 100090","R1L85-C01-01-S2A-20240712|R1L85-C01-02-S2A-20240712|R1L85-C01-03-S2FP-20240712",3,3,1,low,canonical_shadow_only,"source repair required; not production"
```

## 25. Machine-Readable Rows

```jsonl
{"row_type": "price_source_validation", "source": "Songdaiki/stock-web", "source_url": "https://github.com/Songdaiki/stock-web", "manifest_path": "atlas/manifest.json", "schema_path": "atlas/schema.json", "universe_path": "atlas/universe/all_symbols.csv", "manifest_max_date": "2026-02-20", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "calibration_shard_root": "atlas/ohlcv_tradable_by_symbol_year", "raw_shard_root": "atlas/ohlcv_raw_by_symbol_year", "validation_status": "usable_for_historical_calibration"}
{"row_type": "case", "case_id": "R1L85-C01-01", "symbol": "014620", "company_name": "성광벤드", "round": "R1", "loop": 85, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "INDUSTRIAL_FITTINGS_OFFSHORE_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_ORDER_THEME_HIGH_MAE_FADE", "case_type": "industrial_fittings_order_backlog_margin_positive_with_local_4B_watch", "positive_or_counterexample": "positive", "best_trigger": "R1L85-C01-01-S2A-20240712", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "large_positive_MFE_but_local_4B_required_after_order_MFE", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "C01 can keep Stage2 only when order backlog converts into delivery schedule, ASP/cost pass-through and gross/OP margin bridge."}
{"row_type": "trigger", "trigger_id": "R1L85-C01-01-S2A-20240712", "case_id": "R1L85-C01-01", "symbol": "014620", "company_name": "성광벤드", "round": "R1", "loop": 85, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "INDUSTRIAL_FITTINGS_OFFSHORE_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_ORDER_THEME_HIGH_MAE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|order_backlog_margin_bridge_guardrail|local_4B_timing_after_order_MFE|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-12", "evidence_available_at_that_date": "industrial fittings / LNG-plant / energy EPC order-backlog and delivery-margin bridge proxy; primary contract and margin evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["order_backlog_proxy", "customer_or_EPC_project_proxy", "delivery_margin_proxy"], "stage3_evidence_fields": ["confirmed_backlog_quality", "delivery_schedule", "ASP_or_cost_pass_through", "utilization", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["order_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_order_cancellation_or_project_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/014/014620/2024.csv", "profile_path": "atlas/symbol_profiles/014/014620.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-12", "entry_price": 11540, "MFE_30D_pct": 46.45, "MFE_90D_pct": 46.45, "MFE_180D_pct": 181.63, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -1.13, "MAE_90D_pct": -1.13, "MAE_180D_pct": -1.13, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2025-01-17", "peak_price": 32500, "drawdown_after_peak_pct": -30.62, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.85, "four_b_full_window_peak_proximity": 0.75, "four_b_timing_verdict": "local_4B_watch_after_order_backlog_MFE_if_delivery_margin_bridge_stalls", "four_b_evidence_type": ["order_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_order_cancel_or_margin_break", "trigger_outcome_label": "large_positive_MFE_but_local_4B_required_after_order_MFE", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_2025_window_no_profile_CA_candidate", "same_entry_group_id": "R1L85-C01-01", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L85-C01-01", "trigger_id": "R1L85-C01-01-S2A-20240712", "symbol": "014620", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "raw_component_scores_before": {"order_backlog_score": 50, "delivery_visibility_score": 45, "customer_quality_score": 40, "ASP_or_cost_pass_through_score": 40, "gross_margin_bridge_score": 40, "revision_score": 45, "relative_strength_score": 65, "execution_risk_score": 45, "project_delay_risk_score": 35, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 80, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"order_backlog_score": 50, "delivery_visibility_score": 45, "customer_quality_score": 40, "ASP_or_cost_pass_through_score": 40, "gross_margin_bridge_score": 40, "revision_score": 45, "relative_strength_score": 65, "execution_risk_score": 55, "project_delay_risk_score": 35, "source_quality_score": 10, "4B_watch_score": 80}, "weighted_score_after": 77, "stage_label_after": "Stage2-Actionable + local 4B/margin bridge watch", "changed_components": ["delivery_visibility_score", "ASP_or_cost_pass_through_score", "gross_margin_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C01 requires order backlog to convert into delivery schedule, utilization, ASP/cost pass-through and margin bridge before clean Stage2/Green; order-theme MFE alone is demoted or wrapped with local 4B watch.", "MFE_90D_pct": 46.45, "MAE_90D_pct": -1.13, "score_return_alignment_label": "large_positive_MFE_but_local_4B_required_after_order_MFE", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed"}
{"row_type": "case", "case_id": "R1L85-C01-02", "symbol": "023160", "company_name": "태광", "round": "R1", "loop": 85, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "INDUSTRIAL_FITTINGS_OFFSHORE_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_ORDER_THEME_HIGH_MAE_FADE", "case_type": "industrial_fittings_order_backlog_positive_with_high_MAE_watch", "positive_or_counterexample": "positive", "best_trigger": "R1L85-C01-02-S2A-20240712", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "positive_MFE_but_post_peak_margin_bridge_watch_needed", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "price_source": "Songdaiki/stock-web", "notes": "Fittings cycle MFE should not become clean Green unless backlog quality, delivery timing and margin conversion are repaired."}
{"row_type": "trigger", "trigger_id": "R1L85-C01-02-S2A-20240712", "case_id": "R1L85-C01-02", "symbol": "023160", "company_name": "태광", "round": "R1", "loop": 85, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "INDUSTRIAL_FITTINGS_OFFSHORE_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_ORDER_THEME_HIGH_MAE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|order_backlog_margin_bridge_guardrail|local_4B_timing_after_order_MFE|canonical_archetype_compression", "trigger_type": "Stage2-Actionable", "trigger_date": "2024-07-12", "evidence_available_at_that_date": "industrial fittings / pipe fittings order-cycle and energy EPC delivery-margin proxy; primary backlog and margin evidence pending", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["order_backlog_proxy", "customer_or_EPC_project_proxy", "delivery_margin_proxy"], "stage3_evidence_fields": ["confirmed_backlog_quality", "delivery_schedule", "ASP_or_cost_pass_through", "utilization", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["order_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_order_cancellation_or_project_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/023/023160/2024.csv", "profile_path": "atlas/symbol_profiles/023/023160.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-12", "entry_price": 13410, "MFE_30D_pct": 33.63, "MFE_90D_pct": 33.63, "MFE_180D_pct": 33.63, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -3.43, "MAE_90D_pct": -4.55, "MAE_180D_pct": -4.55, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-07-26", "peak_price": 17920, "drawdown_after_peak_pct": -28.57, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.85, "four_b_full_window_peak_proximity": 0.75, "four_b_timing_verdict": "local_4B_watch_when_fittings_order_MFE_outruns_backlog_margin_confirmation", "four_b_evidence_type": ["order_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_order_cancel_or_margin_break", "trigger_outcome_label": "positive_MFE_but_post_peak_margin_bridge_watch_needed", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_CA_candidates", "same_entry_group_id": "R1L85-C01-02", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L85-C01-02", "trigger_id": "R1L85-C01-02-S2A-20240712", "symbol": "023160", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "raw_component_scores_before": {"order_backlog_score": 50, "delivery_visibility_score": 45, "customer_quality_score": 40, "ASP_or_cost_pass_through_score": 40, "gross_margin_bridge_score": 40, "revision_score": 45, "relative_strength_score": 65, "execution_risk_score": 45, "project_delay_risk_score": 35, "source_quality_score": 20, "4B_watch_score": 45}, "weighted_score_before": 80, "stage_label_before": "Stage2-Actionable", "raw_component_scores_after": {"order_backlog_score": 50, "delivery_visibility_score": 45, "customer_quality_score": 40, "ASP_or_cost_pass_through_score": 40, "gross_margin_bridge_score": 40, "revision_score": 45, "relative_strength_score": 65, "execution_risk_score": 45, "project_delay_risk_score": 35, "source_quality_score": 10, "4B_watch_score": 80}, "weighted_score_after": 77, "stage_label_after": "Stage2-Actionable + local 4B/margin bridge watch", "changed_components": ["delivery_visibility_score", "ASP_or_cost_pass_through_score", "gross_margin_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C01 requires order backlog to convert into delivery schedule, utilization, ASP/cost pass-through and margin bridge before clean Stage2/Green; order-theme MFE alone is demoted or wrapped with local 4B watch.", "MFE_90D_pct": 33.63, "MAE_90D_pct": -4.55, "score_return_alignment_label": "positive_MFE_but_post_peak_margin_bridge_watch_needed", "current_profile_verdict": "current_profile_partially_correct_local_4B_watch_needed"}
{"row_type": "case", "case_id": "R1L85-C01-03", "symbol": "100090", "company_name": "SK오션플랜트", "round": "R1", "loop": 85, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "INDUSTRIAL_FITTINGS_OFFSHORE_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_ORDER_THEME_HIGH_MAE_FADE", "case_type": "offshore_wind_order_theme_high_MAE_counterexample", "positive_or_counterexample": "counterexample", "best_trigger": "R1L85-C01-03-S2FP-20240712", "calibration_usable": true, "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "score_price_alignment": "order_theme_MFE_low_quality_high_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE", "price_source": "Songdaiki/stock-web", "notes": "Offshore/order theme should remain RiskWatch unless backlog conversion, utilization, cost overrun control and project-margin bridge are explicit at entry."}
{"row_type": "trigger", "trigger_id": "R1L85-C01-03-S2FP-20240712", "case_id": "R1L85-C01-03", "symbol": "100090", "company_name": "SK오션플랜트", "round": "R1", "loop": 85, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "fine_archetype_id": "INDUSTRIAL_FITTINGS_OFFSHORE_ORDER_BACKLOG_DELIVERY_MARGIN_BRIDGE_VS_ORDER_THEME_HIGH_MAE_FADE", "loop_objective": "coverage_gap_fill|counterexample_mining|order_backlog_margin_bridge_guardrail|local_4B_timing_after_order_MFE|canonical_archetype_compression", "trigger_type": "Stage2-FalsePositive", "trigger_date": "2024-07-12", "evidence_available_at_that_date": "offshore wind / plant orderbook theme proxy without confirmed backlog conversion, utilization and project-margin bridge", "evidence_source": "source_proxy_only; evidence_url_pending", "stage2_evidence_fields": ["order_backlog_proxy", "customer_or_EPC_project_proxy", "delivery_margin_proxy"], "stage3_evidence_fields": ["confirmed_backlog_quality", "delivery_schedule", "ASP_or_cost_pass_through", "utilization", "gross_or_OP_margin_conversion"], "stage4b_evidence_fields": ["order_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "stage4c_evidence_fields": ["hard_order_cancellation_or_project_margin_break_watch_only"], "price_data_source": "Songdaiki/stock-web", "price_data_repo": "https://github.com/Songdaiki/stock-web", "price_shard_path": "atlas/ohlcv_tradable_by_symbol_year/100/100090/2024.csv", "profile_path": "atlas/symbol_profiles/100/100090.json", "price_basis": "tradable_raw", "price_adjustment_status": "raw_unadjusted_marcap", "stock_web_manifest_max_date": "2026-02-20", "entry_date": "2024-07-12", "entry_price": 14020, "MFE_30D_pct": 10.99, "MFE_90D_pct": 15.55, "MFE_180D_pct": 15.55, "MFE_1Y_pct": null, "MFE_2Y_pct": null, "MAE_30D_pct": -26.53, "MAE_90D_pct": -26.53, "MAE_180D_pct": -26.53, "MAE_1Y_pct": null, "below_entry_price_flag_30D": true, "below_entry_price_flag_90D": true, "peak_date": "2024-09-24", "peak_price": 16200, "drawdown_after_peak_pct": -10.31, "green_lateness_ratio": "not_applicable", "four_b_local_peak_proximity": 0.35, "four_b_full_window_peak_proximity": 0.3, "four_b_timing_verdict": "order_theme_rejected_without_backlog_delivery_utilization_margin_bridge", "four_b_evidence_type": ["order_MFE_without_margin_bridge", "post_peak_drawdown", "source_proxy_gap"], "four_c_protection_label": "hard_4C_requires_non_price_order_cancel_or_margin_break", "trigger_outcome_label": "order_theme_MFE_low_quality_high_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE", "calibration_usable": true, "forward_window_trading_days": 180, "calibration_block_reasons": [], "corporate_action_window_status": "clean_2024_window_after_old_2022_CA_candidate", "same_entry_group_id": "R1L85-C01-03", "dedupe_for_aggregate": true, "aggregate_group_role": "representative", "is_new_independent_case": true, "reuse_reason": null, "independent_evidence_weight": 1.0, "do_not_count_as_new_case": false}
{"row_type": "score_simulation", "profile_id": "e2r_2_1_stock_web_calibrated_proxy", "case_id": "R1L85-C01-03", "trigger_id": "R1L85-C01-03-S2FP-20240712", "symbol": "100090", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "raw_component_scores_before": {"order_backlog_score": 25, "delivery_visibility_score": 15, "customer_quality_score": 20, "ASP_or_cost_pass_through_score": 10, "gross_margin_bridge_score": 5, "revision_score": 15, "relative_strength_score": 35, "execution_risk_score": 80, "project_delay_risk_score": 70, "source_quality_score": 15, "4B_watch_score": 70}, "weighted_score_before": 58, "stage_label_before": "Stage2-Watch/FalsePositive", "raw_component_scores_after": {"order_backlog_score": 25, "delivery_visibility_score": 0, "customer_quality_score": 20, "ASP_or_cost_pass_through_score": 0, "gross_margin_bridge_score": 0, "revision_score": 15, "relative_strength_score": 35, "execution_risk_score": 90, "project_delay_risk_score": 70, "source_quality_score": 5, "4B_watch_score": 85}, "weighted_score_after": 45, "stage_label_after": "Rejected-Stage2 / Order-theme RiskWatch", "changed_components": ["delivery_visibility_score", "ASP_or_cost_pass_through_score", "gross_margin_bridge_score", "source_quality_score", "execution_risk_score", "4B_watch_score"], "component_delta_explanation": "C01 requires order backlog to convert into delivery schedule, utilization, ASP/cost pass-through and margin bridge before clean Stage2/Green; order-theme MFE alone is demoted or wrapped with local 4B watch.", "MFE_90D_pct": 15.55, "MAE_90D_pct": -26.53, "score_return_alignment_label": "order_theme_MFE_low_quality_high_MAE_false_positive", "current_profile_verdict": "current_profile_false_positive_high_MAE"}
{"row_type": "shadow_weight", "axis": "C01_order_backlog_delivery_margin_bridge_required", "scope": "canonical_archetype_specific", "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "baseline_value": 0, "tested_value": 1, "delta": "+1", "reason": "Industrial order/backlog rerating requires backlog quality, delivery schedule, utilization, ASP/cost pass-through and margin conversion; order-theme MFE without bridge fades into high MAE or needs local 4B watch.", "backtest_effect": "keeps 014620/023160 with local 4B or margin-bridge watch; demotes 100090 order-theme high-MAE false positive", "trigger_ids": "R1L85-C01-01-S2A-20240712|R1L85-C01-02-S2A-20240712|R1L85-C01-03-S2FP-20240712", "calibration_usable_count": 3, "new_independent_case_count": 3, "counterexample_count": 1, "confidence": "low", "proposal_type": "canonical_shadow_only", "notes": "source_proxy_only/evidence_url_pending; not production"}
{"row_type": "residual_contribution", "round": "R1", "loop": 85, "large_sector_id": "L1_INDUSTRIALS_INFRA_DEFENSE_GRID", "canonical_archetype_id": "C01_ORDER_BACKLOG_MARGIN_BRIDGE", "new_independent_case_count": 3, "reused_case_count": 0, "new_symbol_count": 3, "new_trigger_family_count": 3, "tested_existing_calibrated_axes": ["stage2_actionable_evidence_bonus", "price_only_blowoff_blocks_positive_stage", "full_4b_requires_non_price_evidence", "hard_4c_thesis_break_routes_to_4c", "source_proxy_only_blocks_runtime_promotion", "high_MAE_guardrail", "local_4B_watch_before_full_4B_when_MFE_outruns_bridge"], "residual_error_types_found": ["industrial_order_theme_false_positive_high_MAE", "order_backlog_delivery_margin_bridge_required", "local_4B_late_after_order_MFE", "source_proxy_runtime_promotion_risk", "high_MAE_positive_Green_blocker"], "loop_contribution_label": "canonical_archetype_rule_candidate", "do_not_propose_new_weight_delta": true}
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
- For C01, test a canonical-archetype guard requiring backlog quality, delivery schedule, utilization, ASP/cost pass-through and gross/OP margin conversion before clean Stage2/Green.

## 27. Next Round State

```text
completed_round = R1
completed_loop = 85
next_round = R2
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
